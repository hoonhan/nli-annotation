from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.db import transaction
from rest_framework.decorators import api_view

from scipy import spatial
import json, pickle, random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import random

from .models import Premise, User, Issue, Submit, WordCnt
from .models import VUser, VSubmit, VPair

@csrf_exempt
def checkUser(request):
    mturk_id = request.GET['mturk_id']
    user_type = request.GET['user_type']

    if request.method == 'GET':
        user, created = User.objects.get_or_create(mturk_id=mturk_id)
        if created:
            user.set_type(user_type)
        response = {
            'predone': user.preSurveyDone,
            'step': user.step,
            'user_type': user.user_type
        }
        return JsonResponse(response)

@csrf_exempt
def recordIntroDone(request):
    mturk_id = request.GET['mturk_id']

    if request.method == 'GET':
        user = User.objects.get(mturk_id=mturk_id)
        user.introEnd()
        return HttpResponse('')

@csrf_exempt
def recordPreDone(request):
    if request.method == 'GET':
        mturk_id = request.GET['mturk_id']
        user = User.objects.get(mturk_id=mturk_id)
        user.preDone()
        return HttpResponse('')

@csrf_exempt
def getPremise(request):
    if request.method == 'GET':
        mturk_id = request.GET['mturk_id']
        user = User.objects.get(mturk_id=mturk_id)
        # context_step = 0으로 
        response = {
            'predone': user.preSurveyDone,
            'step': user.step,
            'premise': Premise.objects.get(id=user.step).text
        }
        return JsonResponse(response)

def getRule():
    wordcnt = WordCnt.objects.filter(tot_cnt__gte = 10).values_list('word', 'ent_pmi', 'neu_pmi', 'con_pmi')
    ent_rule = wordcnt.order_by('ent_pmi').first()[0]
    neu_rule = wordcnt.order_by('neu_pmi').first()[0]
    con_rule = wordcnt.order_by('con_pmi').first()[0]
    return [ent_rule, neu_rule, con_rule]

@csrf_exempt
def getPremiseWithRule(request):
    if request.method == 'GET':
        mturk_id = request.GET['mturk_id']
        user = User.objects.get(mturk_id=mturk_id)
        # context_step = 0으로 

        response = {
            'predone': user.preSurveyDone,
            'step': user.step,
            'premise': Premise.objects.get(id=user.step).text,
            'rule': getRule()
        }
    return JsonResponse(response)




@csrf_exempt
def recordIssue(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        step = data['step']
        issue = data['issue']
        rules = data['rules']

        user = User.objects.get(mturk_id=mturk_id)
        premise = Premise.objects.get(id=step).text
        Issue.objects.create(user=user,
                            premise=premise,
                            text=issue,
                            rule_ent = rules[0],
                            rule_neu = rules[1],
                            rule_con = rules[2])
        return HttpResponse('')

def updateWordCnt(sentence, type):
    tokenizer = RegexpTokenizer(r"[\w']+")
    tokens = tokenizer.tokenize(sentence.lower())
    c = Counter(tokens)

    for word, cnt in c.items():
        wordcnt, created = WordCnt.objects.get_or_create(word=word)
        wordcnt.update(type, cnt)

@csrf_exempt
def recordSubmit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        step = data['step']
        entailment = data['entailment']
        neutral = data['neutral']
        contradiction = data['contradiction']
        rule_word = data.get('rules', ['', '', ''])

        user = User.objects.get(mturk_id=mturk_id)
        now_premise = Premise.objects.get(id=step).text
        next_premise = Premise.objects.get(id=step+1).text
        user.step_up()

        with transaction.atomic():
            updateWordCnt(entailment, 'ent')
            updateWordCnt(neutral, 'neu')
            updateWordCnt(contradiction, 'con')

        Submit.objects.create(user=user,
                            premise=now_premise,
                            entailment=entailment,
                            neutral=neutral,
                            contradiction=contradiction,
                            rule_ent = rule_word[0],
                            rule_neu = rule_word[1],
                            rule_con = rule_word[2])
    
        response = {
            'premise': next_premise,
            'rule': getRule()
        }
        return JsonResponse(response)

def extract_keywords(sentence, stop_words):
    sentence_without_stopwords = list(filter(lambda x: x not in stop_words, word_tokenize(sentence)))
    keywords = list(map(lambda x: x[0], filter(lambda x: x[1] == 'NN', nltk.pos_tag(sentence_without_stopwords))))
    return list(set(keywords))

def get_sum_embeddings(word, words, embeddings_dict):
    return sum(map(lambda x: spatial.distance.euclidean(embeddings_dict[word], embeddings_dict[x]),words))

def find_closest_embeddings(words, embeddings_dict):
    return sorted(embeddings_dict.keys(), key=lambda word: get_sum_embeddings(word, words, embeddings_dict))


@csrf_exempt
def resetContext(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        user = User.objects.get(mturk_id=mturk_id)
        premise = Premise.objects.get(id=user.step).text

        user.ctxt_step_reset()
        user.ctxt_step_up()

        embeddings_dict = pickle.load(open('/backend/server/utils/glove_vectors.pkl', 'rb'))
        with open('/backend/server/utils/stopwords.txt', 'r') as f:
            stop_words = f.read().split('\n')
        kwds = extract_keywords(premise, stop_words)
        similar_words = find_closest_embeddings(kwds, embeddings_dict)[:1000]
        response = { 
            'contexts': similar_words[995:1000]
        } 
        return JsonResponse(response)


@csrf_exempt
def newContext(request):
    if request.method == 'GET':
        mturk_id = request.GET['mturk_id']
        user = User.objects.get(mturk_id=mturk_id)
        premise = Premise.objects.get(id=user.step).text
        ctxt_step = user.context_step

        user.ctxt_step_up()

        embeddings_dict = pickle.load(open('/backend/server/utils/glove_vectors.pkl', 'rb'))
        with open('/backend/server/utils/stopwords.txt', 'r') as f:
            stop_words = f.read().split('\n')

        kwds = extract_keywords(premise, stop_words)
        similar_words = find_closest_embeddings(kwds, embeddings_dict)[:1000]
        response = {
            'contexts': similar_words[995-50*(ctxt_step-1):1000-50*(ctxt_step-1)]
        }
        return JsonResponse(response) 



#########################################################
@csrf_exempt
def checkUserVal(request):
    mturk_id = request.GET['mturk_id']

    if request.method == 'GET':
        user, created = VUser.objects.get_or_create(mturk_id=mturk_id)

        response = {
            'step': user.step,
            'is_quit': user.isQuit
        }
        return JsonResponse(response)

@csrf_exempt
def getPairVal(request):
    mturk_id = request.GET['mturk_id']

    if request.method == 'GET':
        user = VUser.objects.get(mturk_id=mturk_id)
        seen_pairs = list(set(VSubmit.objects.filter(user=user).values_list('pair_id', flat=True)))
        gold_pairs = {
            2: 1516,
            5: 1517,
            10: 1518,
            20: 1519,
            30: 1520
        }
        if user.step in gold_pairs.keys():
            pair = VPair.objects.get(id=gold_pairs[user.step])
        else:
            possible_ids = list(VPair.objects.exclude(id__in=seen_pairs+list(gold_pairs.keys())).filter(count__lt=4).values_list('id', flat=True))
            if possible_ids == []:
                response = {
                    'is_quit': True
                }
                return JsonResponse(response)
            
            pk = random.choice(possible_ids)
            pair = VPair.objects.get(id=pk)
        response = {
            'step': user.step,
            'pair_id': pair.id,
            'premise': pair.premise,
            'hypothesis': pair.hypothesis,
            'is_quit': user.isQuit
        }
        return JsonResponse(response)

@csrf_exempt
def submitVal(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        step = data['step']
        pair_id = data['pair_id']
        label = data['label']

        user = VUser.objects.get(mturk_id=mturk_id)
        user.step_up()

        pair = VPair.objects.get(id=pair_id)
        pair.submit()

        VSubmit.objects.create(user=user,
                            pair=pair,
                            label=label)

        response = {
            'step': user.step
        }
        return JsonResponse(response)

@csrf_exempt
def quitVal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        user = VUser.objects.get(mturk_id=mturk_id)
        user.quit()

        return JsonResponse({})
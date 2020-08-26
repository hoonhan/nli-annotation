from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view

from scipy import spatial
import json, pickle, random
import nltk
from nltk.tokenize import word_tokenize 

from .models import Premise, User, Issue, Submit

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

@csrf_exempt
def recordIssue(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        step = data['step']
        issue = data['issue']

        user = User.objects.get(mturk_id=mturk_id)
        premise = Premise.objects.get(id=step).text
        Issue.objects.create(user=user,
                            premise=premise,
                            text=issue)
        return HttpResponse('')


@csrf_exempt
def recordSubmit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mturk_id = data['mturk_id']
        step = data['step']
        entailment = data['entailment']
        neutral = data['neutral']
        contradiction = data['contradiction']

        user = User.objects.get(mturk_id=mturk_id)
        now_premise = Premise.objects.get(id=step).text
        next_premise = Premise.objects.get(id=step+1).text
        user.step_up()
        Submit.objects.create(user=user,
                            premise=now_premise,
                            entailment=entailment,
                            neutral=neutral,
                            contradiction=contradiction)
        return HttpResponse(next_premise)

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
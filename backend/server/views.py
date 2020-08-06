from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
import json

from .models import Premise, User, Issue, Submit

@csrf_exempt
def checkUser(request):
    mturk_id = request.GET['mturk_id']

    if request.method == 'GET':
        user, created = User.objects.get_or_create(mturk_id=mturk_id)
        response = {
            'predone': user.preSurveyDone,
            'step': user.step
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
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    class UserTypes(models.IntegerChoices):
        BASELINE = 0
        ARTIFICIAL = 1
        NATURAL = 2
    mturk_id = models.TextField()
    step = models.IntegerField(default=1)
    context_step = models.IntegerField(default=1)
    user_type = models.IntegerField(choices=UserTypes.choices, default=0)
    preSurveyDone = models.BooleanField(default=False)

    joinTime = models.TimeField(auto_now_add=True)
    introEndTime = models.TimeField(default=timezone.now)
    preEndTime = models.TimeField(default=timezone.now)

    def set_type(self, type):
        self.user_type = type

    def step_up(self):        
        self.step += 1
        self.save()

    def ctxt_step_up(self):
        self.context_step += 1
        self.save()

    def ctxt_step_reset(self):
        self.context_step = 1
        self.save()

    def introEnd(self):
        self.introEndTime = timezone.now()
        self.save()

    def preDone(self):
        self.preSurveyDone = True
        self.preEndTime = timezone.now()
        self.save()

class Premise(models.Model):
    text = models.TextField()

class Issue(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    premise = models.TextField(max_length=300)
    text = models.TextField(max_length=300)
    time = models.TimeField(auto_now_add=True)

class Submit(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    premise = models.TextField(max_length=300)
    entailment = models.TextField(max_length=300)
    neutral = models.TextField(max_length=300)
    contradiction = models.TextField(max_length=300)
    context = models.TextField(max_length=300, default='')
    time = models.TimeField(auto_now_add=True)

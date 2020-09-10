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
    ctype = models.IntegerField(default=0)
    context_step = models.IntegerField(default=1)
    user_type = models.IntegerField(choices=UserTypes.choices, default=0)
    preSurveyDone = models.BooleanField(default=False)

    joinTime = models.DateTimeField(auto_now_add=True)
    introEndTime = models.DateTimeField(default=timezone.now)
    preEndTime = models.DateTimeField(default=timezone.now)

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

    def set_ctype(self, ctype):
        self.ctype = ctype
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
    time = models.DateTimeField(auto_now_add=True)
    premise = models.TextField(max_length=300)
    text = models.TextField(max_length=300)
    rule_ent = models.CharField(max_length=50, default='')
    rule_neu = models.CharField(max_length=50, default='')
    rule_con = models.CharField(max_length=50, default='')


class Submit(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    premise = models.TextField(max_length=300)
    entailment = models.TextField(max_length=300)
    neutral = models.TextField(max_length=300)
    contradiction = models.TextField(max_length=300)
    context = models.TextField(max_length=300, default='')
    rule_ent = models.CharField(max_length=50, default='')
    rule_neu = models.CharField(max_length=50, default='')
    rule_con = models.CharField(max_length=50, default='')

class WordCnt(models.Model):
    word = models.CharField(max_length=50, default='')
    alpha = models.IntegerField(default=5)
    ent_cnt = models.IntegerField(default=0)
    ent_pmi = models.FloatField(default=0)
    neu_cnt = models.IntegerField(default=0)
    neu_pmi = models.FloatField(default=0)
    con_cnt = models.IntegerField(default=0)
    con_pmi = models.FloatField(default=0)
    tot_cnt = models.IntegerField(default=0)

    def update(self, type, cnt):
        if type == 'ent':
            self.ent_cnt += cnt
        elif type == 'neu':
            self.neu_cnt += cnt
        elif type == 'con':
            self.con_cnt += cnt
        elif type == 'update':
            pass #Just to update pmi values
        else:
            raise Exception("Invalid type when updating word count")

        self.tot_cnt = self.ent_cnt + self.neu_cnt + self.con_cnt
        self.ent_pmi = (self.ent_cnt + self.alpha) / (self.tot_cnt + 3 * self.alpha)
        self.neu_pmi = (self.neu_cnt + self.alpha) / (self.tot_cnt + 3 * self.alpha)
        self.con_pmi = (self.con_cnt + self.alpha) / (self.tot_cnt + 3 * self.alpha)

        self.save()


#####################################################

class VUser(models.Model):
    mturk_id = models.TextField()
    step = models.IntegerField(default=1)
    isQuit = models.BooleanField(default=False)

    joinTime = models.DateTimeField(auto_now_add=True)
    quitTime = models.DateTimeField(default=timezone.now)

    def step_up(self):        
        self.step += 1
        self.save()
    
    def quit(self):
        self.isQuit = True
        self.quitTime = timezone.now()
        self.save()

class VPair(models.Model):
    premise = models.TextField(default='')
    hypothesis = models.TextField(default='')
    answer = models.TextField(default='')
    count = models.IntegerField(default=0)

    def submit(self):
        self.count += 1
        self.save()

class VSubmit(models.Model):
    class Types(models.IntegerChoices):
        ERROR = 0
        ENTAILMENT = 1
        NEUTRAL = 2
        CONTRADICTION = 3
        NA = 4
        
    user = models.ForeignKey('VUser', on_delete=models.CASCADE)
    pair = models.ForeignKey('VPair', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    label = models.IntegerField(choices=Types.choices, default=0)

#####################################################


class CIssue(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    premise = models.TextField(max_length=300, default='')
    ctype = models.IntegerField(default=0)
    text = models.TextField(max_length=300)
    cwords = models.TextField(max_length=300, default='')
    cword = models.CharField(max_length=50, default='')


class CSubmit(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    premise = models.TextField(max_length=300)
    ctype = models.IntegerField(default=0)
    text = models.TextField(max_length=300)
    cwords = models.TextField(max_length=300, default='')
    cword = models.CharField(max_length=50, default='')


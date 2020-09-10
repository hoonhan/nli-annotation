from django.urls import path
from . import views

urlpatterns = [
    path('get_premise/', views.getPremise),
    path('get_premise_with_rule/', views.getPremiseWithRule),
    path('check_user/', views.checkUser),
    path('record_intro_done/', views.recordIntroDone),
    path('record_pre_done/', views.recordPreDone),
    path('record_submit/', views.recordSubmit),
    path('record_issue/', views.recordIssue),
    path('new_context/', views.newContext),
    path('reset_context/', views.resetContext),

    path('check_user_val/', views.checkUserVal),
    path('get_pair_val/', views.getPairVal),
    path('submit_val/', views.submitVal),
    path('quit_val/', views.quitVal),

    path('record_submit_cword/', views.recordSubmitCWord),
    path('get_cword/', views.getCWord),
    path('record_issue_cword/', views.recordIssueCWord)
]
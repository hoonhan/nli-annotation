from django.urls import path
from . import views

urlpatterns = [
    path('get_premise/', views.getPremise),
    path('check_user/', views.checkUser),
    path('record_intro_done/', views.recordIntroDone),
    path('record_pre_done/', views.recordPreDone),
    path('record_submit/', views.recordSubmit),
    path('record_issue/', views.recordIssue)
]
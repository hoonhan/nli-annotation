from django.contrib import admin

# Register your models here.
from .models import Premise, VPair

admin.site.register(Premise)
admin.site.register(VPair)
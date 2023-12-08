from django.contrib import admin
from . import models
from tweetapp.models import tweet

# Register your models here.

class tweetadmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]}),
    ]
    #fields = ['nickname']

admin.site.register(tweet,tweetadmin)
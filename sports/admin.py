from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(SportsHouse)
admin.site.register(SportsEvent)
class Details(admin.ModelAdmin):
    list_display = ['event_name','event_dateTime','rank1','rank2','rank3']
    list_editable=['event_dateTime','rank1','rank2','rank3']
admin.site.register(SportsEventDetail,Details)

class Participant(admin.ModelAdmin):
    list_display=['__str__','participant_house','participant_score','participant_event_1','participant_event_2','participant_event_3']
    list_editable=['participant_score']
    ordering=['participant_name']
admin.site.register(SportsParticipant,Participant)
admin.site.register(SportsGallery)  


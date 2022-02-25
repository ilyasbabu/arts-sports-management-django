from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(SportsHouse)
admin.site.register(SportsEvent)
admin.site.register(SportsEventDetail)

class Participant(admin.ModelAdmin):
    list_display=['__str__','participant_score','participant_event_1','participant_event_2','participant_event_3']
    list_editable=['participant_score']
admin.site.register(SportsParticipant,Participant)
admin.site.register(SportsGallery)  

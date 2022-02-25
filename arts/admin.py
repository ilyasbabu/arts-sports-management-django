from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ArtsHouse)
admin.site.register(ArtsEvent)
admin.site.register(ArtsEventDetail)
class Participant(admin.ModelAdmin):
    list_display=['__str__','participant_house','participant_score','participant_event_1','participant_event_2','participant_event_3']
    list_editable=['participant_score']
    ordering=['participant_name']
admin.site.register(ArtsParticipant,Participant)
admin.site.register(ArtsGallery)

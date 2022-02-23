from django.db import models

# Create your models here.
class ArtsHouse(models.Model):
    house_name=models.CharField(max_length=10)
    def __str__(self):
        return self.house_name
        

class ArtsEvent(models.Model):
    event_name=models.CharField(max_length=100)
    def __str__(self):
        return self.event_name

class ArtsEventDetail(models.Model):
    event_name=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE)
    event_date=models.DateField()
    event_time=models.TimeField()


class ArtsParticipant(models.Model):
    participant_name=models.CharField(max_length=100)
    participant_department=models.CharField(max_length=100)
    participant_house=models.ForeignKey(ArtsHouse,on_delete=models.CASCADE)
    participant_score=models.IntegerField(null=True,blank=True)
    participant_event_1=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_1')
    participant_event_2=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_2')
    participant_event_3=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_3')
    def __str__(self):
        return self.participant_name
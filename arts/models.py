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
    event_dateTime=models.DateTimeField()
    #event_time=models.CharField(max_length=10)


class ArtsParticipant(models.Model):
    participant_name=models.CharField(max_length=100)
    participant_email=models.EmailField()
    participant_mobile=models.IntegerField()
    participant_department=models.CharField(max_length=100)
    participant_year=models.CharField(max_length=15)
    participant_house=models.ForeignKey(ArtsHouse,on_delete=models.CASCADE)
    participant_score=models.IntegerField(null=True,blank=True)
    participant_event_1=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_1')
    participant_event_2=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_2')
    participant_event_3=models.ForeignKey(ArtsEvent,on_delete=models.CASCADE,null=True,blank=True,related_name='participant_event_3')
    def __str__(self):
        return self.participant_name

class ArtsGallery(models.Model):
    image_name=models.CharField(max_length=100)
    image_desc=models.TextField()
    image_file=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.image_name
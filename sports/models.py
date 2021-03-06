from django.db import models

# Create your models here.
class SportsHouse(models.Model):
    house_name=models.CharField(max_length=10)
    def __str__(self):
        return self.house_name

class SportsEvent(models.Model):
    event_name=models.CharField(max_length=100)
    def __str__(self):
        return self.event_name


class SportsParticipant(models.Model):
    participant_name=models.CharField(max_length=100)
    participant_email=models.EmailField()
    participant_mobile=models.CharField(max_length=12)
    participant_department=models.CharField(max_length=100)
    participant_year=models.CharField(max_length=15)
    participant_house=models.ForeignKey(SportsHouse,on_delete=models.CASCADE)
    participant_score=models.IntegerField(null=True,blank=True)
    participant_event_1=models.ForeignKey(SportsEvent,on_delete=models.CASCADE,related_name='participant_event_1')
    participant_event_2=models.ForeignKey(SportsEvent,on_delete=models.CASCADE,default=0,null=True,blank=True,related_name='participant_event_2')
    participant_event_3=models.ForeignKey(SportsEvent,on_delete=models.CASCADE,default=0,null=True,blank=True,related_name='participant_event_3')
    def __str__(self):
        return self.participant_name

class SportsGallery(models.Model):
    event_name=models.ForeignKey(SportsEvent,on_delete=models.CASCADE)
    year=models.IntegerField()
    image_file=models.ImageField(upload_to='images/')

class SportsEventDetail(models.Model):
    event_name=models.ForeignKey(SportsEvent,on_delete=models.CASCADE)
    event_dateTime=models.DateTimeField()
    rank1=models.ForeignKey(SportsParticipant,on_delete=models.CASCADE,null=True,blank=True,related_name='rank1')
    rank2=models.ForeignKey(SportsParticipant,on_delete=models.CASCADE,null=True,blank=True,related_name='rank2')
    rank3=models.ForeignKey(SportsParticipant,on_delete=models.CASCADE,null=True,blank=True,related_name='rank3')
    def __str__(self):
        return self.event_name.event_name

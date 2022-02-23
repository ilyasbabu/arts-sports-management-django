from django import forms
from .models import *


class SportsRegForm(forms.ModelForm):
    class Meta:
        sem=(
        ('',"Select Semester"),
        ('s1',"1st Semester"),
        ('s2',"2nd Semester"),
        ('s3',"3rd Semester"),
        ('s4',"4th Semester"),
        ('s5',"5th Semester"),
        ('s6',"6th Semester"),
        ('s7',"7th Semester"),
        ('s8',"8th Semester"),
    )
        model = SportsParticipant
        fields = '__all__'
        exclude = ['participant_score']
        widgets = {
            'participant_name': forms.TextInput(attrs={'class': 'form-control w-11/12','placeholder':'Enter your name'}),
            'participant_email': forms.EmailInput(attrs={'class': 'form-control w-11/12','placeholder':'Enter your email'}),
            'participant_mobile': forms.NumberInput(attrs={'class': 'form-control w-11/12','placeholder':'Enter your mobile'}),
            'participant_department': forms.TextInput(attrs={'class': 'form-control w-11/12','placeholder':'Enter your Department'}),
            'participant_semester': forms.Select(attrs={'class': 'form-control w-11/12','placeholder':'Enter your Department'},choices=sem),
            'participant_house': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_1': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_2': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_3': forms.Select(attrs={'class': 'form-control w-full'}),
        }
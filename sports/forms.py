from django import forms
from .models import *


class SportsRegForm(forms.ModelForm):
    class Meta:
        sem=(
        ('',"Select Year of study"),
        ('1st',"1st Year"),
        ('2nd',"2nd Year"),
        ('3rd',"3rd Year"),
    )
        model = SportsParticipant
        fields = '__all__'
        exclude = ['participant_score']
        widgets = {
            'participant_name': forms.TextInput(attrs={'class': 'form-control w-full','placeholder':'Enter your name'}),
            'participant_email': forms.EmailInput(attrs={'class': 'form-control w-full','placeholder':'Enter your email'}),
            'participant_mobile': forms.NumberInput(attrs={'class': 'form-control w-full','placeholder':'Enter your mobile'}),
            'participant_department': forms.TextInput(attrs={'class': 'form-control w-full','placeholder':'Enter your Department'}),
            'participant_year': forms.Select(attrs={'class': 'form-control w-full','placeholder':'Enter your Department'},choices=sem),
            'participant_house': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_1': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_2': forms.Select(attrs={'class': 'form-control w-full'}),
            'participant_event_3': forms.Select(attrs={'class': 'form-control w-full'}),
        }
from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def sportshome(request):
    return render(request, 'sports.html')
def sportsdetails(request):
    return render(request, 'sportsdetails.html')
def sportsgallery(request):
    return render(request, 'sports_gallery.html')
def sports_score(request):
    return render(request, 'sports_score.html')
def sports_register(request):
    form=SportsRegForm(request.POST)
    if request.method=='POST':
        participant_name=request.POST.get('participant_name')
        participant_email=request.POST.get('participant_email')
        participant_mobile=request.POST.get('participant_mobile')
        participant_department=request.POST.get('participant_department')
        participant_semester=request.POST.get('participant_semester')
        participant_house=request.POST.get('participant_house')
        participant_event_1=request.POST.get('participant_event_1')
        participant_event_2=request.POST.get('participant_event_2')
        participant_event_3=request.POST.get('participant_event_3')
        participant=SportsParticipant(participant_name=participant_name,participant_email=participant_email,participant_mobile=participant_mobile,participant_department=participant_department,participant_semester=participant_semester,participant_house_id=participant_house,participant_event_1_id=participant_event_1,participant_event_2_id=participant_event_2,participant_event_3_id=participant_event_3)
        participant.save()
        return redirect('/')
    return render(request, 'sports_register.html',{'form':form})
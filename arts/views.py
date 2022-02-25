from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def artshome(request):
    return render(request, 'arts.html')
def artsdetails(request):
    return render(request, 'artsdetails.html')
def artsgallery(request):
    return render(request, 'arts_gallery.html')
def arts_score(request):
    return render(request, 'arts_score.html')
def arts_register(request):
    form=ArtsRegForm(request.POST)
    if request.method=='POST':
        participant_name=request.POST.get('participant_name')
        participant_email=request.POST.get('participant_email')
        participant_mobile=request.POST.get('participant_mobile')
        participant_department=request.POST.get('participant_department')
        participant_year=request.POST.get('participant_year')
        participant_house=request.POST.get('participant_house')
        participant_event_1=request.POST.get('participant_event_1')
        participant_event_2=request.POST.get('participant_event_2')
        participant_event_3=request.POST.get('participant_event_3')
        participant=ArtsParticipant(participant_name=participant_name,participant_email=participant_email,participant_mobile=participant_mobile,participant_department=participant_department,participant_year=participant_year,participant_house_id=participant_house,participant_event_1_id=participant_event_1,participant_event_2_id=participant_event_2,participant_event_3_id=participant_event_3)
        participant.save()
        return redirect('/')
    return render(request, 'arts_register.html',{'form':form})
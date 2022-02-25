from django.shortcuts import render,redirect
from .forms import *
from django.db.models import Sum

# Create your views here.
def sportshome(request):
    return render(request, 'sports.html')
def sportsdetails(request):
    return render(request, 'sportsdetails.html')
def sportsgallery(request):
    photos=SportsGallery.objects.all()
    return render(request, 'sports_gallery.html',{'ph':photos})
def sports_score(request):
    dim=SportsParticipant.objects.filter(participant_house_id=1).aggregate(Sum('participant_score'))
    dim=dim['participant_score__sum']
    rub=SportsParticipant.objects.filter(participant_house_id=2).aggregate(Sum('participant_score'))
    rub=rub['participant_score__sum']
    eme=SportsParticipant.objects.filter(participant_house_id=3).aggregate(Sum('participant_score'))
    eme=eme['participant_score__sum']
    sap=SportsParticipant.objects.filter(participant_house_id=4).aggregate(Sum('participant_score'))
    sap=sap['participant_score__sum']
    rank=SportsParticipant.objects.all().order_by('-participant_score')
    return render(request, 'sports_score.html',{'dim':dim,'rub':rub,'eme':eme,'sap':sap,'rank':rank})
def sports_register(request):
    form=SportsRegForm(request.POST)
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
        participant=SportsParticipant(participant_name=participant_name,participant_email=participant_email,participant_mobile=participant_mobile,participant_department=participant_department,participant_year=participant_year,participant_house_id=participant_house,participant_event_1_id=participant_event_1,participant_event_2_id=participant_event_2,participant_event_3_id=participant_event_3)
        participant.save()
        return redirect('/')
    return render(request, 'sports_register.html',{'form':form})
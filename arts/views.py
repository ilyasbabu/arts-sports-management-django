from django.shortcuts import render,redirect
from .forms import *
from django.db.models import Sum,Q
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def artshome(request):
    return render(request, 'arts.html')
    
@login_required(login_url='/')
def artsdetails(request):
    details=ArtsEvent.objects.all()
    schedule=ArtsEventDetail.objects.all().order_by('event_dateTime')
    return render(request, 'artsdetails.html',{'details':details,'schedule':schedule})

@login_required(login_url='/')
def artsgallery(request):
    photos=ArtsGallery.objects.all()
    return render(request, 'arts_gallery.html',{'ph':photos})

@login_required(login_url='/')
def artgallerysearch(request):
    query=None
    if 'q' in request.GET:
        query=request.GET.get("q")
        print (query)
        photos=ArtsGallery.objects.all().filter(
            Q(event_name__event_name__icontains=query) 
            |
            Q(year__icontains=query)
        )
    return render (request, 'arts_gallery.html',{'ph':photos})

@login_required(login_url='/')
def arts_score(request):
    sap=ArtsParticipant.objects.filter(participant_house_id=1).aggregate(Sum('participant_score'))
    sap=sap['participant_score__sum']
    eme=ArtsParticipant.objects.filter(participant_house_id=2).aggregate(Sum('participant_score'))
    eme=eme['participant_score__sum']
    rub=ArtsParticipant.objects.filter(participant_house_id=3).aggregate(Sum('participant_score'))
    rub=rub['participant_score__sum']
    dim=ArtsParticipant.objects.filter(participant_house_id=4).aggregate(Sum('participant_score'))
    dim=dim['participant_score__sum']
    rank=ArtsParticipant.objects.all().order_by('-participant_score')
    event=ArtsEventDetail.objects.all().order_by('rank1')
    return render(request, 'arts_score.html',{'dim':dim,'rub':rub,'eme':eme,'sap':sap,'rank':rank,'event':event})

@login_required(login_url='/')
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
        return redirect('/arts/')
    return render(request, 'arts_register.html',{'form':form})

def error_404(request, exception):
    return render(request, '404.html')
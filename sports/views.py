from django.shortcuts import render
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
    form=SportsRegForm()
    return render(request, 'sports_register.html',{'form':form})
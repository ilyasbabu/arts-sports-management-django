from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def artshome(request):
    return render(request, 'arts.html')
def sportshome(request):
    return render(request, 'sports.html')
def artsdetails(request):
    return render(request, 'artsdetails.html')
def sportsdetails(request):
    return render(request, 'sportsdetails.html')
def artsgallery(request):
    return render(request, 'arts_gallery.html')
def sportsgallery(request):
    return render(request, 'sports_gallery.html')
def arts_score(request):
    return render(request, 'arts_score.html')
def sports_score(request):
    return render(request, 'sports_score.html')
def arts_register(request):
    return render(request, 'arts_register.html')
def sports_register(request):
    return render(request, 'sports_register.html')
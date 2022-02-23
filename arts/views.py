from django.shortcuts import render

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
    return render(request, 'arts_register.html')
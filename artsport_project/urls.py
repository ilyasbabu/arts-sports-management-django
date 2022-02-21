"""artsport_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.home, name='home'),
    path('arts/',views.artshome,name='artshome'),
    path('sports/',views.sportshome,name='sportshome'),
    path('arts/details/',views.artsdetails,name='artsdetails'),
    path('sports/details/',views.sportsdetails,name='sportsdetails'),
    path('arts/gallery/',views.artsgallery,name='artsgallery'),
    path('sports/gallery/',views.sportsgallery,name='sportsgallery'),
    path('arts/score/',views.arts_score,name='arts_score'),
    path('sports/score/',views.sports_score,name='sports_score'),
    path('arts/register',views.arts_register,name='arts_register'),
    path('sports/register',views.sports_register,name='sports_register'),
]

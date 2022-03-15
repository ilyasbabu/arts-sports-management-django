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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from mainapp import views as mainapp_views
from arts import views as artsviews
from sports import views as sportsviews
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', mainapp_views.home, name='home'),
    path('arts/',artsviews.artshome,name='artshome'),
    path('sports/',sportsviews.sportshome,name='sportshome'),
    path('arts/details/',artsviews.artsdetails,name='artsdetails'),
    path('sports/details/',sportsviews.sportsdetails,name='sportsdetails'),
    path('arts/gallery/',artsviews.artsgallery,name='artsgallery'),
    path('sports/gallery/',sportsviews.sportsgallery,name='sportsgallery'),
    path('arts/score/',artsviews.arts_score,name='arts_score'),
    path('sports/score/',sportsviews.sports_score,name='sports_score'),
    path('arts/register',artsviews.arts_register,name='arts_register'),
    path('sports/register',sportsviews.sports_register,name='sports_register'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'arts.views.error_404'

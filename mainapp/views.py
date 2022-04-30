from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import AdmissionNumbers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def home(request):
#     adm=request.POST.get('admission')
#     print (adm)
#     return render(request, 'index.html')

def v_login(request):
    numbers=AdmissionNumbers.objects.all()
    numbers=numbers.values_list('admission_number',flat=True)
    if request.method=="POST":
        adm=request.POST.get("admission")
        print (adm)
        if adm in numbers:
            username="student"
            password="azeez@123"
            user=authenticate(username=username,password=password)
            print (user)
            if user is not None: #check if the value of user variable is not None
                if user.is_active:
                    login(request,user)
                    return render(request,"index.html")
                else:
                    print('gagal')
                    return redirect('/')
            
        else:
            messages.warning(request,'wrong admission number !!')
            logout(request)
            return redirect("/")
    return render(request, 'login.html')

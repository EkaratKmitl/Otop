from django.shortcuts import render

from django.http import HttpResponse #ประกาศดึง ฟังชั้น มาใช้งาน,

from django.contrib.auth.forms import AuthenticationForm



def index(request):             
    return render(request, 'index.html')

def home2(request):
    return render(request, 'Page2.html')

def home3(request):
    return render(request, 'Page3.html')

def home4(request):
    return render(request, 'Page4.html')

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'account/login.html')


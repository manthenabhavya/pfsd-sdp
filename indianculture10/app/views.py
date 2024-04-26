from django.shortcuts import *

# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    return render(request,"signup.html")

def contactus(request):
    return render(request,"contactus.html")

def aboutus(request):
    return render(request,"aboutus.html")

def offerings(request):
    return render(request,"offerings.html")
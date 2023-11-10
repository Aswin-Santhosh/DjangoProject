from django.shortcuts import render

# Create your views here.


def UserRegistration(request):
    return render(request,"Guest/UserRegistration.html")


def UserLogin(request):
    return render(request,"Guest/Login.html")

def HomePage(request):
    return render(request,"Guest/home.html")

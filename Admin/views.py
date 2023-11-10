from django.shortcuts import render,redirect

# Create your views here.


def District(request):
    return render(request,"Admin/District.html")


def homePage(request):
    return render(request,"Admin/Home.html")


def Place(request):
    return render(request,"Admin/Place.html")
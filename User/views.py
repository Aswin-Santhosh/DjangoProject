from django.shortcuts import render

# Create your views here.



def ChangePassword(request):
    return render(request,"User/ChangePassword.html")


def EditProfile(request):
    return render(request,"User/EditProfile.html")

def MyProfile(request):
    return render(request,"User/MyProfile.html")

def Home(request):
    return render(request,"User/Home.html")


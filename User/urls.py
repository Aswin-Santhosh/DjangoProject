from django.contrib import admin
from django.urls import path
from User import views

app_name="wuser"

urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
]

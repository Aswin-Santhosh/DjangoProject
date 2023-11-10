from django.contrib import admin
from django.urls import path
from Guest import views

app_name="wguest"


urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name="UserRegistration"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('HomePage/',views.HomePage,name="HomePage"),
]

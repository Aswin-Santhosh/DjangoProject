from django.urls import path
from Admin import views

app_name="wadmin"


urlpatterns = [
 
    path('District/',views.District,name="District"),
    path('Place/',views.Place,name="Place"),
    path('homePage/',views.homePage,name="homePage"),
    
]

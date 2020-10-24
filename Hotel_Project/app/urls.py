from app import views
from django.urls import path


urlpatterns = [
    
    path('', views.home, name = 'home'),
    #path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('services/', views.services, name = 'services'),
    path('booking/', views.booking, name = 'booking'),
    path('glogin/', views.glogin, name = 'glogin'),
    path('glogout/', views.glogout, name = 'glogout'),

    ]
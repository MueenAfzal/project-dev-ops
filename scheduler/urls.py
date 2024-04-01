
from django.contrib import admin
from django.urls import path,include
from scheduler import views

urlpatterns = [ # Include authentication URLs
     path('', views.index, name='index'),
     path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.about, name='about'),
    
]

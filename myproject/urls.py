
from django.contrib import admin
from django.urls import path,include
from scheduler import views

urlpatterns = [
 
    path('admin/', admin.site.urls),
     path('', include('scheduler.urls')),

]

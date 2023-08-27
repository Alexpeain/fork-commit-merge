# Django - Easy

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #TODO: Add /hello path here 
    path('hello/',include('hello_world_app.urls')),
]

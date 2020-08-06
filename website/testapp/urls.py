from django.conf.urls import url
from django.contrib import admin
from .views import testappTest
from .views import Home,Employees,testappTest


urlpatterns = [
   
    url(r'^home/',Home),
    url(r'^employee/',Employees),
    url(r'^testapptest/',testappTest),  
]
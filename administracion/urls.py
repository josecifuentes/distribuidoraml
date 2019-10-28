from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employee/new', views.newemployee, name='newemployee'),
    path('employee', views.listemployee, name='listemployee'),
    
    ]
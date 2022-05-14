from django.contrib import admin
from django.urls import path, include
from .views import index, listTkt, createTkt, tktdetails, manageTkt

urlpatterns = [
    path('', index, name='home'),
    path('list/', listTkt, name='list'),
    path('create/', createTkt, name='create'),
    path('details/<int:id>/', tktdetails, name='details'),
     path('manage/', manageTkt, name='manage'),

]

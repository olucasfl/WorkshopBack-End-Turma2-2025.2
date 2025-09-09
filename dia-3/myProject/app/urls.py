from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
#    path('', views.get_users, name='get_users'),
    path('', views.index),
    path('user/<str:nick>', views.get_user_by_nick),
    path('data/', views.user_manager),
    
]
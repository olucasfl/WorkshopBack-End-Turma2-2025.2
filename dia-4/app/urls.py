from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar-cep/', views.buscar_cep, name='buscar_cep'),
]

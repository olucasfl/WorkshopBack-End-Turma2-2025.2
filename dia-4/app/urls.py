from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/consultar-cep', views.viaCepFormView.as_view(), name='buscar_cep'),
    
]

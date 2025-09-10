from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.viaCepFormView.as_view(), name='buscar_cep'),
    path('ceps/', views.ViaCepListView.as_view(), name='list_ceps'),
    path('ceps/<int:pk>/', views.ViaCepDetailView.as_view(), name='detail_cep'),
    path('ceps/<int:pk>/delete/', views.ViaCepDeleteView.as_view(), name='delete_cep'),
]
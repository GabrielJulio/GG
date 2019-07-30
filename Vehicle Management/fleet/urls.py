from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fleet_principal'),
    path('viagem/', views.listagem, name='listagem_viagem')
]
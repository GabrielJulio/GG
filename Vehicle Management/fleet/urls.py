from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fleet_principal'),
    path('viagem/', views.listagem_viagem, name='listagem_viagem'),
    path('viagem/nova', views.nova_viagem, name='nova_viagem'),
    path('motorista/', views.listagem_motorista, name='listagem_motorista'),
    path('motorista/novo', views.novo_motorista, name='novo_motorista'),
    path('veiculo/', views.listagem_veiculo, name='listagem_veiculo'),
    path('veiculo/novo', views.novo_veiculo, name='novo_veiculo'),
]
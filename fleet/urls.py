from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='pgprincipal'),
    path('login/', LoginView.as_view(), name='entrar'),
    path('logout/', views.meu_logout, name='sair'),

    path('viagem/nova', views.nova_viagem, name='nova_viagem'),
    path('viagem/atualizar/<int:id>', views.atualizar_viagem, name='atualizar_viagem'),
    path('viagem/apagar/<int:id>', views.apagar_viagem, name='apagar_viagem'),

    path('motorista/novo', views.novo_motorista, name='novo_motorista'),
    path('motorista/atualizar/<int:id>', views.atualizar_motorista, name='atualizar_motorista'),
    path('motorista/apagar/<int:id>', views.apagar_motorista, name='apagar_motorista'),

    path('veiculo/novo', views.novo_veiculo, name='novo_veiculo'),
    path('veiculo/atualizar/<int:id>', views.atualizar_veiculo, name='atualizar_veiculo'),
    path('veiculo/apagar/<int:id>', views.apagar_veiculo, name='apagar_veiculo'),
]


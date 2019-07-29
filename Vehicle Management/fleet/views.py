from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import  redirect
from .models import Viagem, Motorista, Veiculo

def home(request):
	return render(request, 'index.html')

def meu_logout(request):
    logout(request)
    return redirect('/')

def index(request):
	return render(request, 'fleet/index.html')

def listagem(request):
	data = {}
	data['viagens'] = Viagem.objects.all()
	return render(request, 'fleet/listagem.html', data)

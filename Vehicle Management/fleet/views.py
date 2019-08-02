from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import  redirect
from .models import Viagem, Motorista, Veiculo
from .form import VeiculoForm, MotoristaForm, ViagemForm

def home(request):
	return render(request, 'index.html')


def meu_logout(request):
    logout(request)
    return redirect('/')


def index(request):
	return render(request, 'fleet/index.html')


def listagem_viagem(request):
	data = {}
	data['viagens'] = Viagem.objects.all()
	return render(request, 'fleet/read/viagem.html', data)


def listagem_motorista(request):
	data = {}
	data['motoristas'] = Motorista.objects.all()
	return render(request, 'fleet/read/motorista.html', data)


def listagem_veiculo(request):
	data = {}
	data['veiculos'] = Veiculo.objects.all()
	return render(request, 'fleet/read/veiculo.html', {'data': data})


def nova_viagem(request):
	form = ViagemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/viagem')
	return render(request, 'fleet/create/form.html', {'form': form})


def novo_veiculo(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/veiculo')
	return render(request, 'fleet/create/form.html', {'form': form})


def novo_motorista(request):
	form = MotoristaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/motorista')
	return render(request, 'fleet/create/form.html', {'form': form})

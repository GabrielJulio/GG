from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import Viagem, Motorista, Veiculo
from .form import VeiculoForm, MotoristaForm, ViagemForm


def home(request):
	return render(request, 'index.html')


def meu_logout(request):
    logout(request)
    return redirect('/')


def index(request):
	return render(request, 'fleet/index.html')


def nova_viagem(request):
	form = ViagemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/viagem')
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})


def listagem_viagem(request):
	data = {}
	data['viagens'] = Viagem.objects.all()
	return render(request, 'fleet/read/viagem.html', data)


def atualizar_viagem(request, id):
	viagem = get_object_or_404(Viagem, pk=id)
	form = ViagemForm(request.POST or None, instance=viagem)
	if form.is_valid():
		form.save()
		return redirect('listagem_viagem')
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})


def apagar_viagem(request, id):
	viagem = Viagem.objects.get(pk=id)
	if request.method == 'POST':
		viagem.delete()
		return redirect('listagem_viagem')
	return render(request, 'fleet/delete/confirmacao.html', {'viagem': viagem})


def novo_motorista(request):
	form = MotoristaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/motorista')
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})


def listagem_motorista(request):
	data = {}
	data['motoristas'] = Motorista.objects.all()
	return render(request, 'fleet/read/motorista.html', data)


def atualizar_motorista(request, id):
	motorista = get_object_or_404(Motorista, pk=id)
	form = MotoristaForm(request.POST or None, instance=motorista)
	if form.is_valid():
		form.save()
		return redirect('listagem_motorista')
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})


def apagar_motorista(request, id):
	motorista = Motorista.objects.get(pk=id)
	if request.method == "POST":
		motorista.delete()
		return redirect('listagem_motorista')
	return render(request, 'fleet/delete/confirmacao.html', {'motorista': motorista})

def novo_veiculo(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/frota/veiculo')
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})


def listagem_veiculo(request):
	data = {}
	data['veiculos'] = Veiculo.objects.all()
	return render(request, 'fleet/read/veiculo.html', data)


def atualizar_veiculo(request, id):
	veiculo = get_object_or_404(Veiculo, pk=id)
	form = VeiculoForm(request.POST or None, instance=veiculo)
	if form.is_valid():
		form.save()
		return redirect("listagem_veiculo")
	return render(request, 'fleet/formularios/form_cadastro.html', {'form': form})

def apagar_veiculo(request, id):
	veiculo = Veiculo.objects.get(pk=id)
	if request.method == 'POST':
		veiculo.delete()
		return redirect('listagem_veiculos')
	return render(request, 'fleet/delete/confirmacao.html', {'veiculo': veiculo})
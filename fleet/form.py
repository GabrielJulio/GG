from django.forms import ModelForm
from .models import Viagem, Veiculo, Motorista

class ViagemForm(ModelForm):
	class Meta:
		model = Viagem
		fields = [
			'veiculo',
			'motorista',
			'data',
			'saida',
			'retorno',
			'observacoes',
		]

class VeiculoForm(ModelForm):
	class Meta:
		model = Veiculo
		fields = [
			'tipo_veiculo',
			'nome',
			'marca',
			'ano',
			'placa',
			'observacoes'
		]

class MotoristaForm(ModelForm):
	class Meta:
		model = Motorista
		fields = [
			'nome',
			'cpf',
			'data_nascimento',
			'observacoes'
		]

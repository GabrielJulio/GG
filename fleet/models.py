from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Veiculo(models.Model):
	CARRO = "Carro"
	MOTO = "Moto"
	TIPO_VEICULO_ESCOLHAS = [
		(CARRO, "Carro"),
		(MOTO, "Moto"),
	]
	tipo_veiculo = models.CharField(max_length=5, choices=TIPO_VEICULO_ESCOLHAS, default=CARRO)
	nome = models.CharField(max_length=50)
	marca = models.CharField(max_length=40, null=True)
	ano = models.IntegerField(validators=[MinValueValidator(0, None), MaxValueValidator(9999, None)])
	placa = models.CharField(max_length=8, null=True)
	observacoes = models.TextField(max_length=1500, blank=True)

	def __str__(self):
		return self.nome


class Motorista(models.Model):
	nome = models.CharField(max_length=50)
	cpf = models.CharField(max_length=14, null=True)
	data_nascimento = models.DateField("data de nascimento", null=True)
	observacoes = models.TextField(max_length=1500, blank=True)

	def __str__(self):
		return self.nome


class Viagem(models.Model):
	veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
	motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)
	data = models.DateField("data da viagem")
	saida = models.TimeField("horario da saida")
	retorno = models.TimeField("horario do retorno", null=True, blank=True)
	observacoes = models.TextField(max_length=1500, blank=True)

	def __str__(self):
		return "Viagem " + str(self.id)

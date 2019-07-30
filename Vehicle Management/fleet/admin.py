from django.contrib import admin
from . models import Veiculo, Motorista, Viagem

# Register your models here.

admin.site.register(Veiculo)
admin.site.register(Motorista)
admin.site.register(Viagem)
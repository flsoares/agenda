from django.contrib import admin
from core.models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):# Definindo os campos que seráo apresentados
    list_display = ('titulo','data_evento','data_criacao')
    list_filter = ('usuario','data_evento',)
# REGISTRANDO O MODELO
admin.site.register(Evento, EventoAdmin)
# Tem que associar a model Evento com a classe EventoAdmin
# Caso contrario os nao ficionará

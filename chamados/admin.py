from django.contrib import admin

from .models import Chamado, Comentario


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'solicitante', 'responsavel', 'status', 'prioridade', 'criado_em')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'chamado', 'autor', 'criado_em')
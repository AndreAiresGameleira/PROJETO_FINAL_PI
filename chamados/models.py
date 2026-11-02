from django.conf import settings
from django.db import models


class Chamado(models.Model):
    class Status(models.TextChoices):
        ABERTO = 'aberto', 'Aberto'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        RESOLVIDO = 'resolvido', 'Resolvido'
        FECHADO = 'fechado', 'Fechado'

    class Prioridade(models.TextChoices):
        BAIXA = 'baixa', 'Baixa'
        MEDIA = 'media', 'Média'
        ALTA = 'alta', 'Alta'
        URGENTE = 'urgente', 'Urgente'

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='chamados_abertos',)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='chamados_assumidos',)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.ABERTO,)
    prioridade = models.CharField(max_length=20,choices=Prioridade.choices,default=Prioridade.MEDIA,)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'#{self.pk} {self.titulo}'


class Comentario(models.Model):
    chamado = models.ForeignKey(Chamado,on_delete=models.CASCADE,related_name='comentarios',)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='comentarios_chamados',)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return f'Comentário de {self.autor.get_username()} em #{self.chamado_id}'
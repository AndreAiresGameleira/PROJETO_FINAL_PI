
from django.conf import settings
from django.db import models


class Perfil(models.Model):
    class Tipo(models.TextChoices):
        SOLICITANTE = 'solicitante', 'Solicitante'
        TECNICO = 'tecnico', 'Técnico'
        ADMINISTRADOR = 'administrador', 'Administrador'

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil',
    )
    tipo = models.CharField(
        max_length=20,
        choices=Tipo.choices,
        default=Tipo.SOLICITANTE,
    )
    telefone = models.CharField(max_length=20, blank=True)
    setor = models.CharField(max_length=100, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'
        ordering = ['usuario__username']

    def __str__(self):
        return f'{self.usuario.get_username()} ({self.get_tipo_display()})'

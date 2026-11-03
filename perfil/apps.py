from django.apps import AppConfig


class PerfilConfig(AppConfig):
    name = 'perfil'

    def ready(self):
        from . import signals  # noqa: F401
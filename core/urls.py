from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('perfil/', include('perfil.urls')),
    path('chamados/', include('chamados.urls')),
]
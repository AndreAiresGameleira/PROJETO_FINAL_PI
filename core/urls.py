from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('perfil/', include('perfil.urls')),
    path('chamados/', include('chamados.urls')),
]
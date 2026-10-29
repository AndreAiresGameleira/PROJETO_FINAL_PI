from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', login_view, name ='login'),
    path('logout/', logout, name='logout'),
    path('lista_usu/', lista_usuarios, name ='lista_usu'),
    path('criar_usu/', criar_usuario, name ='cria_usu'),
    path('dasativar_usu/', desativar_usuario, name ='desativar_usu'),
]

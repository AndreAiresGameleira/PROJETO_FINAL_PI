from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('usuarios/', views.lista_usuarios, name='lista_usu'),
    path('usuarios/criar_usu/', views.criar_usuario, name='criar_usu'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/desativar_usu/', views.desativar_usuario, name='desativar_usu'),
]

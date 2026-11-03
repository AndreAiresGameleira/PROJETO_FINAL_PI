from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('tecnico/', views.lista_tecnico, name='lista_tecnico'),
    path('administrador/', views.lista_administrador, name='lista_administrador'),

    path('novo/', views.criar_chamado, name='criar_chamado'),

    path('<int:pk>/', views.detalhe_chamado, name='detalhe_chamado'),
    path('<int:pk>/tecnico/', views.detalhe_chamado_tecnico, name='detalhe_chamado_tecnico'),
    path('<int:pk>/administrador/', views.detalhe_chamado_admin, name='detalhe_chamado_admin'),

    path('<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('<int:pk>/comentar/tecnico/', views.adicionar_comentario_tecnico, name='adicionar_comentario_tecnico'),
    path('<int:pk>/comentar/administrador/', views.adicionar_comentario_admin, name='adicionar_comentario_admin'),
    path('<int:pk>/assumir/', views.assumir_chamado, name='assumir_chamado'),
    path('<int:pk>/status/', views.atualizar_status, name='atualizar_status'),
]

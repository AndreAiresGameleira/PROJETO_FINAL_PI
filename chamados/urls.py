from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('novo/', views.criar_chamado, name='criar_chamado'),
    path('<int:pk>/', views.detalhe_chamado, name='detalhe_chamado'),
    path('<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('<int:pk>/assumir/', views.assumir_chamado, name='assumir_chamado'),
    path('<int:pk>/status/', views.atualizar_status, name='atualizar_status'),
]

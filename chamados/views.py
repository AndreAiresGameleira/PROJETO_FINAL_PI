from django.shortcuts import render

def lista_chamados(request):
    return render(request, 'chamados/lista_chamados.html', {})

def criar_chamado(request):
    return render(request, 'chamados/criar_chamado.html', {})

def detalhe_chamado(request):
    return render(request, 'chamados/detalhe_chamado.html', {})

def adicionar_comentario(request):
    return render(request, 'chamados/adicionar_comentario.html', {})

def assumir_chamado(request):
    return render(request, 'chamados/assumir_chamado.html', {})

def atualizar_status(request):
    return render(request, 'chamados/atualizar_status.html', {})

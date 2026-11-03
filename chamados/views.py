from django.shortcuts import render, redirect


def lista_chamados(request):
    return render(request, 'chamados/lista_solicitante.html', {})

def lista_tecnico(request):
    return render(request, 'chamados/lista_tecnico.html', {})

def lista_administrador(request):
    return render(request, 'chamados/lista_administrador.html', {})

def criar_chamado(request):
    return render(request, 'chamados/criar_chamado.html', {})

def detalhe_chamado(request, pk):
    return render(request, 'chamados/detalhe_chamado.html', {})

def detalhe_chamado_tecnico(request, pk):
    return render(request, 'chamados/detalhe_chamado_tecnico.html', {})

def detalhe_chamado_admin(request, pk):
    return render(request, 'chamados/detalhe_chamado_admin.html', {})

def adicionar_comentario(request, pk):
    return redirect('detalhe_chamado', pk=pk)

def adicionar_comentario_tecnico(request, pk):
    return redirect('detalhe_chamado_tecnico', pk=pk)

def adicionar_comentario_admin(request, pk):
    return redirect('detalhe_chamado_admin', pk=pk)

def assumir_chamado(request, pk):
    return redirect('lista_tecnico')

def atualizar_status(request, pk):
    return redirect('detalhe_chamado_tecnico', pk=pk)

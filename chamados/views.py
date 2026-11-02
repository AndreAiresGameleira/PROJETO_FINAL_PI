from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Chamado, Comentario
from .forms import ChamadoForm, ComentarioForm


def verificar_tipo(usuario):
    perfil = getattr(usuario, 'perfil', None)
    if perfil:
        return perfil.tipo

    return None


@login_required
def lista_chamados(request):

    tipo = verificar_tipo(request.user)

    # Área do técnico
    if tipo == 'tecnico':

        chamados_disponiveis = Chamado.objects.filter(
            responsavel__isnull=True,
            status=Chamado.Status.ABERTO
        )

        meus_chamados = Chamado.objects.filter(
            responsavel=request.user
        )

        return render(request, 'chamados/lista_tecnico.html', {
            'chamados_disponiveis': chamados_disponiveis,
            'meus_chamados': meus_chamados,
        })

    # Área do solicitante
    elif tipo == 'solicitante':

        chamados = Chamado.objects.filter(
            solicitante=request.user
        )

        return render(request, 'chamados/lista_solicitante.html', {
            'chamados': chamados,
        })

    # Área do administrador
    elif tipo == 'administrador':

        chamados = Chamado.objects.all()

        return render(request, 'chamados/lista_administrador.html', {
            'chamados': chamados,
        })

    return render(request, 'chamados/sem_perfil.html')


@login_required
def criar_chamado(request):

    if verificar_tipo(request.user) != 'solicitante':
        return redirect('lista_chamados')

    if request.method == 'POST':
        form = ChamadoForm(request.POST)

        if form.is_valid():
            chamado = form.save(commit=False)

            # Define automaticamente quem abriu o chamado
            chamado.solicitante = request.user

            chamado.save()

            messages.success(request, 'Chamado criado com sucesso!')

            return redirect('lista_chamados')

    else:
        form = ChamadoForm()

    return render(request, 'chamados/criar_chamado.html', {
        'form': form
    })


@login_required
def detalhe_chamado(request, pk):

    chamado = get_object_or_404(Chamado, pk=pk)

    tipo = verificar_tipo(request.user)

    # O solicitante só pode ver os próprios chamados
    if tipo == 'solicitante' and chamado.solicitante != request.user:
        return redirect('lista_chamados')

    # O técnico só pode ver chamados disponíveis ou que assumiu
    if tipo == 'tecnico':
        if chamado.responsavel != request.user and chamado.responsavel is not None:
            return redirect('lista_chamados')

    comentarios = chamado.comentarios.all()

    return render(request, 'chamados/detalhe_chamado.html', {
        'chamado': chamado,
        'comentarios': comentarios,
        'form': ComentarioForm(),
    })


@login_required
@require_POST
def adicionar_comentario(request, pk):

    chamado = get_object_or_404(Chamado, pk=pk)

    tipo = verificar_tipo(request.user)

    permitido = (
        chamado.solicitante == request.user
        or chamado.responsavel == request.user
        or tipo == 'administrador'
    )

    if not permitido:
        return redirect('lista_chamados')

    form = ComentarioForm(request.POST)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.chamado = chamado
        comentario.autor = request.user
        comentario.save()

        messages.success(request, 'Comentário adicionado!')

    return redirect('detalhe_chamado', pk=pk)


@login_required
@require_POST
def assumir_chamado(request, pk):

    if verificar_tipo(request.user) != 'tecnico':
        return redirect('lista_chamados')

    # Só permite assumir se ainda estiver disponível
    quantidade = Chamado.objects.filter(
        pk=pk,
        responsavel__isnull=True,
        status=Chamado.Status.ABERTO
    ).update(
        responsavel=request.user,
        status=Chamado.Status.EM_ANDAMENTO
    )

    if quantidade:
        messages.success(request, 'Você assumiu o chamado!')
    else:
        messages.error(request, 'Esse chamado já foi assumido ou não está disponível.')

    return redirect('lista_chamados')


@login_required
@require_POST
def atualizar_status(request, pk):

    chamado = get_object_or_404(Chamado, pk=pk)

    tipo = verificar_tipo(request.user)

    if chamado.responsavel != request.user and tipo != 'administrador':
        return redirect('lista_chamados')

    novo_status = request.POST.get('status')

    status_validos = [valor for valor, rotulo in Chamado.Status.choices]

    if novo_status in status_validos:
        chamado.status = novo_status
        chamado.save()

        messages.success(request, 'Status atualizado!')

    return redirect('detalhe_chamado', pk=pk)
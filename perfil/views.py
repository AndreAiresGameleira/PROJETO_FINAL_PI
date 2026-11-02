
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm, LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('lista_chamados')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('lista_chamados')
    else:
        form = LoginForm(request)

    return render(request, 'perfil/login.html', {'form': form})
@login_required
def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/')

    return render(request, 'perfil/logout.html')



def lista_usuarios(request):
    return render(request, 'perfil/lista_usu.html', {})



def criar_usuario(request):
    return render(request, 'perfil/criar_usu.html', {})



def editar_usuario(request, pk):
    return render(request, 'perfil/editar_usu.html', {})



def desativar_usuario(request, pk):
    return render(request, 'perfil/desativar_usu.html', {})

from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request, 'perfil/login.html', {})

def logout_view(request):
    return render(request, 'perfil/logout.html', {})

def lista_usuarios(request):
    return render(request, 'perfil/lista_usu.html', {})

def criar_usuario(request):
    return render(request, 'perfil/criar_usu.html', {})

def desativar_usuario(request):
    return render(request, 'perfil/desativar_usu.html', {})

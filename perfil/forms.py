from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['usuario', 'tipo', 'telefone', 'setor']
        labels = {
            'usuario': '',
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário'
        })
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        })
    )
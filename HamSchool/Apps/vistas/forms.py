from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth.models import User


class CustomCreationForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pass','placeholder' : 'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pass','placeholder' : 'Confirmar Contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'registar','placeholder' : 'Nombre de usuario', 'autocomplete':"off"}),
            'first_name': forms.TextInput(attrs={'class': 'registar','placeholder' : 'Nombres', 'autocomplete':"off"}),
            'last_name': forms.TextInput(attrs={'class': 'registar','placeholder' : 'Apellidos', 'autocomplete':"off"}),
            'email': forms.TextInput(attrs={'class': 'registar','placeholder' : 'Email', 'autocomplete':"off"}),
        }


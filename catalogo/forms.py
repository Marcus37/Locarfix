from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['username','email','nome','sexo','cpf','endereco']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['username','email','nome','sexo','cpf','endereco','is_active','is_staff']
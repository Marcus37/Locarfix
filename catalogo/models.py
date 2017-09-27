from django.db import models

import re
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.

sex = (
    ('M','Masculino'),
    ('F','Feminino'),
    ('O','Outros')
)

class Categoria(models.Model):
    tipo_vec = models.CharField('Tipo do Veiculo',max_length=50)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    def __str__(self):
        return self.tipo_vec

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['tipo_vec']

class Veiculo(models.Model):
    placa = models.CharField('Placa',max_length=50, unique=True)
    renavan = models.CharField('Renavan',max_length=50, unique=True)
    modelo = models.CharField('Modelo',max_length=50)
    marca = models.CharField('Marca',max_length=50)
    cor = models.CharField('Cor',max_length=50)
    ano_mod = models.PositiveIntegerField('Ano do Modelo')
    ano_vec = models.PositiveIntegerField('Ano de Fabricação')
    categoria = models.ForeignKey('catalogo.Categoria',verbose_name='Categoria')
    preco_al = models.DecimalField('Preço do aluguel', decimal_places=2, max_digits=11)
    vec_foto = models.ImageField(blank=True,upload_to="catalogo/veiculoimg")

    created = models.DateTimeField('Criado em',auto_now_add=True)
    modified = models.DateTimeField('Modificado em',auto_now_add=True)

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['marca']



class Cliente(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email',max_length=100)
    sexo = models.CharField(max_length=100, choices=sex, default="M", verbose_name="Sexo", blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    endereco = models.CharField('Endereço', max_length=100,blank=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nome','cpf']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]



class Aluguel(models.Model):
    cliente = models.ForeignKey('catalogo.Cliente',verbose_name='Cliente')
    veiculo = models.ForeignKey('catalogo.Veiculo',verbose_name= 'Veículo')

    def __str__(self):
        return self.cliente.nome

    aluguel = models.DateTimeField('Alugado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"
        ordering = ['cliente']

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=100)
    sexo = models.CharField(max_length=100, choices=sex, default="M", verbose_name="Sexo", blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    data_nasc = models.DateField('Data de Nascimento', max_length=20)
    enderco = models.CharField('Endereço', max_length=100, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ['nome']
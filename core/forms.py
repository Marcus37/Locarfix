# coding=utf-8

from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',required=True)
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea())

    # def __init__(self, *args, **kwargs):
    #     super(ContatoForm, self).__init__(*args, **kwargs)
    #     self.fields['nome'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['mensagem'].widget.attrs['class'] = 'form-control'


class PesquisaVeiculoForm(forms.Form):
    nome = forms.CharField(label='Nome', required=True)


class PesquisaAluguelForm(forms.Form):
    dataInicial = forms.DateField(label='Data Inicial',widget=forms.SelectDateWidget())
    dataFinal = forms.DateField(label='Data Final', widget=forms.SelectDateWidget())


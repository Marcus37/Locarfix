from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin

from core.forms import ContatoForm, PesquisaVeiculoForm, PesquisaAluguelForm
from  catalogo.models import Categoria,Veiculo, Aluguel, Cliente , Funcionario
from django.core.mail import send_mail


from catalogo.forms import UserAdminCreationForm

# Create your views here.

#Cliente = get_user_model()


def index(request):

    return render(request,'index.html')


# def veiculos(request):
#     return render(request,'veiculo_list.html')

def contact(request):
    sucesso = False
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            send_mail('LocarFix',mensagem,email,['FHULVIO_ANDRADE@outlook.com'])
            sucesso = True
    else:
        form = ContatoForm()
    context = {
            'form': form,
            'sucesso': sucesso
    }
    return render(request, 'contact.html', context)

def PesquisaVeiculo(request):
    # sucesso = False
    if request.method == 'POST':
        form = PesquisaVeiculoForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['nome']
            veiculo = Veiculo.objects.filter(marca__icontains=marca)
            context = {
                'veiculos': veiculo,
            }
            return render(request, 'catalogo/veiculos_por_categoria.html', context)
            sucesso = True

    else:
        form = PesquisaVeiculoForm()
        context = {
            'form': form,
        }
    return render(request, 'pesquisa_veiculo.html',context)

def PesquisaAluguel(request):
    # sucesso = False
    if request.method == 'POST':
        form = PesquisaAluguelForm(request.POST)
        if form.is_valid():
            dataInicial = form.cleaned_data['dataInicial']
            dataFinal = form.cleaned_data['dataFinal']
            aluguel = Aluguel.objects.filter(aluguel__range=(dataInicial,dataFinal))
            context = {
                'alugueis': aluguel,
            }
            return render(request, 'catalogo/aluguel_list.html', context)
            sucesso = True

        else:
            context= {
                'form': form,
            }

    else:
        form = PesquisaAluguelForm()
        context = {
            'form': form,
        }
    return render(request, 'pesquisa_aluguel.html',context)

class RegistroFuncView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'Registro_Func.html'
    model = Funcionario
    success_url = reverse_lazy('minha_conta')

registro_func = RegistroFuncView.as_view()

class RegistroView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'registro.html'
    model = Cliente
    success_url = reverse_lazy('index')

registro = RegistroView.as_view()

class AluguelView(CreateView):
    template_name = 'registro_aluguel.html'
    model = Aluguel
    fields = ['cliente','veiculo']
    success_url = reverse_lazy('index')

aluguel = AluguelView.as_view()


class UpdateFunc(LoginRequiredMixin,UpdateView):
    model = Funcionario
    template_name = 'update_func.html'
    fields = ['nome','email','endereco','sexo','funcao']

    def get_object(self):
        return self.request.user

    success_url = reverse_lazy('minha_conta')

update_func = UpdateFunc.as_view()

class ContaView(LoginRequiredMixin,TemplateView):
    template_name = "minha_conta.html"

contaView = ContaView.as_view()

class UpdateCliente(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = 'update_cliente.html'
    fields = ['nome','email','endereco','sexo']

    def get_object(self):
        return self.request.user

    success_url = reverse_lazy('minha_conta')

update_cliente = UpdateCliente.as_view()

class AlterarSenhaView(LoginRequiredMixin,FormView):
    template_name = "alterar_senha.html"
    success_url = reverse_lazy('minha_conta')
    form_class = PasswordChangeForm
    def get_form_kwargs(self):
        kwargs = super(AlterarSenhaView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(AlterarSenhaView,self).form_valid(form)

alterarSenha = AlterarSenhaView.as_view()

class Registrar_veiculo(CreateView):
    template_name = "registro_veiculo.html"
    model = Veiculo
    fields = ['placa','renavan','modelo','marca','cor','ano_mod','ano_vec','categoria','preco_al','vec_foto']
    success_url = reverse_lazy('minha_conta')

registro_veiculo = Registrar_veiculo.as_view()
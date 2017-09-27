from django.shortcuts import render
from  django.views import generic
# Create your views here.
from django.views.generic import DetailView

from .models import Veiculo,Categoria


class VeiculoView(generic.ListView):
    model = Veiculo
    template_name = 'catalogo/veiculos_por_categoria.html'
    context_object_name = 'veiculo'
    paginate_by = 2

veiculos_por_categoria = VeiculoView.as_view()

# def veiculo_list(request):
#     context = {
#         'veiculos': Veiculo.objects.all(),
#     }
#     return render(request,'catalogo/veiculo_list.html',context)

def categoria_id(request,pk):
    categoria = Categoria.objects.get(id=pk)
    context = {
        'categoria_atual': categoria,
        'veiculos': Veiculo.objects.filter(categoria=categoria),
    }
    return render(request,'catalogo/veiculos_por_categoria.html',context)

def veiculoDetalhes(request,pk):
    veiculo = Veiculo.objects.get(id=pk)
    context = {
        'veiculo' : veiculo,

    }
    return render(request, 'catalogo/detalhes.html', context)

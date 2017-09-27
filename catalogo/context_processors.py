from .models import Categoria,Veiculo

def categorias(request):
    return {
        'categorias': Categoria.objects.all()
    }
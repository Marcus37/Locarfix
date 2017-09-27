from django.contrib import admin

# Register your models here.

from.models import Categoria, Veiculo, Cliente, Aluguel,Funcionario

class VeiculoInline(admin.StackedInline):
    model = Veiculo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['tipo_vec','created','modified']
    search_fields = ['tipo_vec','created']
    list_filter = ['tipo_vec']
    inlines = [VeiculoInline]



# class VeiculoAdmin(admin.ModelAdmin):
#     list_display = ['placa','renavan','modelo','marca','cor','ano_mod','ano_vec','categoria',
#                     'preco_v','preco_al','vec_foto','created','modified']
#
#     search_fields = ['placa','renavan','modelo','marca','cor','ano_mod','ano_vec','categoria',
#                     'preco_v','preco_al']
#     list_filter = ['placa','modelo','marca','cor','ano_vec','categoria',
#                     'preco_v','preco_al',]

# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ['nome','sex','cpf','data_nasc','ender','created','modified']
#     search_fields = ['nome','sex','cpf','data_nasc','ender','created']
#     list_filter = ['nome','sex','data_nasc','ender']

#class FuncionarioAdmin(admin.ModelAdmin):
 #   list_display = ['nome','sex','cpf','data_nasc','ender','funcao','created','modified']
  #  search_fields = ['nome','sex','cpf','data_nasc','ender','funcao','created']
   # list_filter = ['nome','sex','data_nasc','ender']

class AluguelAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'veiculo', 'aluguel', 'modified']
    search_fields = ['cliente','veiculo','aluguel']
    list_filter = ['cliente', 'veiculo' ]

admin.site.register(Categoria,CategoriaAdmin)

#admin.site.register(Veiculo,VeiculoInline)

admin.site.register(Cliente)

admin.site.register(Funcionario)

admin.site.register(Aluguel,AluguelAdmin)
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.veiculos_por_categoria,name='veiculos_por_categoria'),
    url(r'^([\d]+)/$',views.categoria_id,name='categoria_id'),
    #url(r'^([\d]+)/$',views.veiculoDetalhes,name='veiculo_detalhes'),
]
"""locarfix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from core import views
from catalogo import views as views_catalogo
from locarfix import settings
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^contato/$', views.contact,name='contato'),
    url(r'^pesquisa/$', views.PesquisaVeiculo,name='pesquisa'),
    url(r'^pesquisaAluguel/$', views.PesquisaAluguel,name='pesquisaAluguel'),
    url(r'^login/$', login,{'template_name': 'login.html'},name='login'),
    url(r'^logout/$', logout,{'next_page': 'index'},name='logout'),
    url(r'^registro/$', views.registro,name='registro'),
    url(r'^registro_func/$', views.registro_func,name='registro_func'),
    url(r'^registro_aluguel/$', views.aluguel,name='registro_aluguel'),
    url(r'^registro_veiculo/$', views.registro_veiculo,name='registro_veiculo'),
    url(r'^minha_conta/$', views.contaView,name='minha_conta'),
    url(r'^update_cliente/$', views.update_cliente,name='update_cliente'),
    url(r'^update_func/$', views.update_func,name='update_func'),
    url(r'^alterarSenha/$', views.alterarSenha,name='alterarSenha'),


    # url(r'^veiculos/', views_catalogo.VeiculoView,name='veiculos'),
    #url(r'^veiculos$', views.veiculos,name='veiculos'),

    url(r'^veiculos/', include('catalogo.urls',namespace='catalogo')),

    #url(r'^detalhes/$', views_catalogo.veiculoDetalhes,name='detalhes'),
    url(r'^admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


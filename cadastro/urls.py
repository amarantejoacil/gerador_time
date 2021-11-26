from django.urls import path
from .views import IndexView, CreateJogador, DeleteJogador, CreateConfiguracao, \
    AtualizarConfiguracao
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='pagina-inicial'),
    path('cadastro/', CreateJogador.as_view(), name='cadastro-jogador'),
    path('cadastro/configuracao', CreateConfiguracao.as_view(), name='cadastro-configuracao'),
    path('deletar/<int:pk>', DeleteJogador.as_view(), name='deletar-jogador'),
    path('atualizar/configuracao/<int:pk>', AtualizarConfiguracao.as_view(), name='atualizar-configuracao'),
    path('gerartime/', views.GerarTime, name='gerar-time'),
]
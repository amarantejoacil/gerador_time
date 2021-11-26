from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Jogador, Configuracao
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
import random


class IndexView(ListView):
    model = Jogador
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['configuracao'] = Configuracao.objects.all()
        context['contador'] = Jogador.objects.count()
        return context


class CreateJogador(CreateView):
    model = Jogador
    template_name = 'modelo_formulario.html'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Cadastrar Jogador'
        return context


class DeleteJogador(DeleteView):
    model = Jogador
    success_url = '/'
    template_name = 'modelo_formulario_excluir.html'


class CreateConfiguracao(CreateView):
    model = Configuracao
    template_name = 'modelo_formulario.html'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Cadastrar Configuração'
        return context


class AtualizarConfiguracao(UpdateView):
    model = Configuracao
    fields = '__all__'
    success_url = '/'
    template_name = 'modelo_formulario.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Atualizar Configuração'
        return context


def GerarTime(request):
    configuracao = Configuracao.objects.all()
    ListaJogadores = Jogador.objects.all()
    listapreenchida = []
    for lista in ListaJogadores:
        listapreenchida.append(lista)

    random.shuffle(listapreenchida)

    # fazer regra de negocio

    context = {
        'lista_embaralhada': listapreenchida,
        'configuracao': configuracao
    }

    return render(request, 'time_gerado.html', context)
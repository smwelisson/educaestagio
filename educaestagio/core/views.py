from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Candidato
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy


class CurriculoCreate(CreateView):
    model = Candidato
    fields = ['usuario', 'nome', 'cidade', 'bairro', 'telefone']
    template_name = 'createCurriculo.html'
    success_url = reverse_lazy('candidato')


class CurriculoList(ListView):
    model = Candidato
    template_name = 'candidato.html'


class testeList(ListView):
    model = Candidato
    template_name = 'teste.html'


class CurriculoUpdate(UpdateView):
    model = Candidato
    fields = ['usuario', 'nome', 'cidade', 'bairro', 'telefone']
    template_name = 'editCurriculo.html'
    success_url = reverse_lazy('candidato')


class CurriculoDelete(DeleteView):
    model = Candidato
    template_name = 'delCurriculo.html'
    success_url = reverse_lazy('candidato')



def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def editCurriculo(request):
    return render(request, 'editCurriculo.html')


def editaCurriculo(request):
    return render(request, 'createCurriculo.html')


class UsuarioCreate(CreateView):
    template_name = "account/signup.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # context['titulo'] = 'Registro de novo usuário'
        return context

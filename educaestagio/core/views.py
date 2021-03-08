from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Candidato
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


############### CRUD ###############


class CurriculoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Candidato
    fields = ['nome', 'cidade', 'bairro', 'telefone', 'estado_civil', 'sexo', 'formacao', 'curso']
    template_name = 'formCurriculo/createCurriculo.html'
    success_url = reverse_lazy('candidato')

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


class CurriculoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Candidato
    template_name = 'candidato.html'

    def get_queryset(self):
        self.object_list = Candidato.objects.filter(usuario=self.request.user)
        return self.object_list


class CurriculoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Candidato
    fields = ['nome', 'cidade', 'bairro', 'telefone', 'estado_civil', 'sexo', 'formacao', 'curso']
    template_name = 'formCurriculo/editCurriculo.html'
    success_url = reverse_lazy('candidato')


class CurriculoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Candidato
    template_name = 'formCurriculo/delCurriculo.html'
    success_url = reverse_lazy('candidato')


############### Sigin ###############


class UsuarioCreate(CreateView):
    template_name = "account/signup.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

    def get_context_data(self):
        context = super().get_context_data()

        context['titulo'] = 'Registro de novo usuário'
        context['botao'] = 'Cadastrar'

        return context

# 1q@w3e4r
############### Testes ###############


def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def registro(request):
    return render(request, 'registro.html')




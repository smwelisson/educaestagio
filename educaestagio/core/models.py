from django.db import models
from django.contrib.auth.models import User


class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=10)
    telefone = models.CharField(max_length=11, blank=True)
    estado_civil_choices = [('Casado', 'Casado'), ('Solteiro', 'Solteiro'), ('Viúvo', 'Viúvo')]
    estado_civil = models.CharField(max_length=50, choices=estado_civil_choices, verbose_name='Estado Civil', blank=True)
    sexo_choices = [('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')]
    sexo = models.CharField(max_length=50, choices=sexo_choices, verbose_name='Sexo', blank=True)
    formacao_choices = [
        ('Cursando Técnico', 'Cursando Técnico'), ('Técnico Completo', 'Técnico Completo'),
        ('Cursando Tecnologia', 'Cursando Tecnologia'), ('Tecnologia Completo', 'Tecnologia Completo'),
        ('Cursando Licenciatura', 'Cursando Licenciatura'), ('Licenciatura Completo', 'Licenciatura Completo'),
        ('Cursando Bacharelado', 'Cursando Bacharelado'), ('Bacharelado Completo', 'Bacharelado Completo'),
        ('Cursando Mestrado', 'Cursando Mestrado'), ('Mestrado Completo', 'Mestrado Completo'),
    ]
    formacao = models.CharField(max_length=50, choices=formacao_choices, verbose_name='Formação', blank=True)
    curso = models.CharField(max_length=50)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

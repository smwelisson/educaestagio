from django.db import models
from django.contrib.auth.models import User


class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=10)
    telefone = models.CharField(max_length=11)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
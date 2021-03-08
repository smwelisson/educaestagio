from django.contrib import admin
from .models import Candidato

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade', 'bairro', 'telefone', 'estado_civil', 'sexo', 'formacao', 'curso')
    list_display_links = ('id',)
    list_filter = ('nome',)
    list_per_page = 20

admin.site.register(Candidato, CandidatoAdmin)

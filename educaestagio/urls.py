from django.contrib import admin
from django.urls import path
from educaestagio.core.views import home, login, candidato, empresa, about
from educaestagio.subscriptions.views import subscribe

urlpatterns = [
    path('', home),
    path('login', login),
    path('candidato', candidato),
    path('empresa', empresa),
    path('about', about),
    path('inscricao/', subscribe),
    path('admin/', admin.site.urls),
]

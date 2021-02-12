from django.contrib import admin
from django.urls import path
from educaestagio.core.views import home, login, candidato, empresa, sobre


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('candidato/', candidato, name='candidato'),
    path('empresa/', empresa, name='empresa'),
    path('sobre/', sobre, name='sobre'),
    path('admin/', admin.site.urls),
]

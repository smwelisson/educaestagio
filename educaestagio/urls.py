from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from educaestagio.core.views import home, sobre,\
    UsuarioCreate, CurriculoCreate, CurriculoUpdate, CurriculoDelete, CurriculoList, testeList


urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),

    path('accounts/', include('allauth.urls')),

    path('signup/', UsuarioCreate.as_view(template_name='account/signup.html'), name='registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('createCurriculo/', CurriculoCreate.as_view(), name='createCurriculo'),
    path('candidato/', CurriculoList.as_view(), name='candidato'),

    path('editCurriculo/<int:pk>/', CurriculoUpdate.as_view(), name='editCurriculo'),
    path('delCurriculo/<int:pk>/', CurriculoDelete.as_view(), name='delCurriculo'),

    path('teste/', testeList.as_view(), name='teste'),
    path('admin/', admin.site.urls),
]

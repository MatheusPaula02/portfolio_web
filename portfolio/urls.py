from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre', views.sobre_mim, name='sobre'),
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('projeto/<str:id_projeto>/', views.detalhes_projetos, name='detalhes_projeto'),
]
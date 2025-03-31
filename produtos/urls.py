from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar, name='visualizar'),  # Rota para /produtos/
    path('cadastro/', views.cadastrar, name='cadastrar'),  # Rota para /produtos/cadastro/
]
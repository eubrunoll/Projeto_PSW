from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'produtos/cadastro.html')  # Certifique-se de que 'cadastro.html' existe na pasta de templates
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        produto = Produto(
            nome=nome,
            preco=preco
        )
        produto.save()

        return HttpResponse("Produto cadastrado com sucesso!")

def visualizar(request):
    return HttpResponse("Página de visualização de produtos")
from produto.models import Produto
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'


class ProdutoDetalhes(View):
    pass


class AdicionarCarrinho(View):
    pass


class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass

# Create your views here.

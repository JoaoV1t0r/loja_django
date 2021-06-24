from django.urls import path
from . import views

app_name = 'produto'

urslpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.ProdutoDetalhes.as_view(), name='detalhe'),
    path('adicionarcart/', views.ProdutoDetalhes.as_view(), name='adicionar_cart'),
    path('removercart/', views.ProdutoDetalhesas_.view(), name='remover_cart'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]

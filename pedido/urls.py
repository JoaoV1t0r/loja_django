from django.urls import path
from . import views

app_name = 'pedido'

urslpatterns = [
    path('', views.Pagar.as_view(), name='pagar'),
    path('fecharpedido/', views.FecharPedido.as_view(), name='fechar_pedido'),
    path('detalhes/', views.DetalhePedido.as_view(), name='detalhes'),
]

from pedido.models import ItemPedido, Pedido
from django.contrib import admin


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)

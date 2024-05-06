# admin.py en tu aplicación de pedidos

from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'creado_en', 'actualizado_en', 'activo']
    list_filter = ['activo', 'creado_en']
    search_fields = ['usuario__username']

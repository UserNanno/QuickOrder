# tasks.py en tu aplicación de pedidos

from celery import shared_task
from .models import Pedido

@shared_task
def process_order(pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    # Lógica para procesar el pedido
    print(f"Procesando el pedido {pedido.id}")

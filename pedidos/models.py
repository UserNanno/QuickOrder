# models.py en tu aplicación de pedidos

from django.db import models
from django.conf import settings
from menus.models import MenuItem

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    items = models.ManyToManyField(MenuItem)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Pedido {self.id} de {self.usuario.username}'

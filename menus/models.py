# models.py en tu aplicación de menús

from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2)  # Ejemplo: 9999.99

    def __str__(self):
        return self.name

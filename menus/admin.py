# admin.py en tu aplicación de menús

from django.contrib import admin
from .models import MenuItem

admin.site.register(MenuItem)

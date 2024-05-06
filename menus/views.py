# views.py en tu aplicación de menús

from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from .models import MenuItem
from django.views.generic import TemplateView


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menus/menu.html'
    context_object_name = 'menu_items'

class SubmitOrderView(View):
    def post(self, request, *args, **kwargs):
        selected_items = request.POST.getlist('menu_item')
        # Aquí puedes procesar los ítems seleccionados, como guardar un pedido en la base de datos
        print("Items seleccionados:", selected_items)  # Solo para demostración
        # Redirige a una página de éxito
        return HttpResponseRedirect(reverse_lazy('order_success'))

    # Opcional: Maneja el caso de GET si es necesario
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('menu'))


class OrderSuccessView(TemplateView):
    template_name = 'menus/order_success.html'

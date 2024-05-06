# views.py en tu aplicación de pedidos

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views import View
from .models import Pedido
from menus.models import MenuItem
from django.views.generic import TemplateView
from .tasks import process_order


class SubmitOrderView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        selected_items_ids = request.POST.getlist('menu_item')
        selected_items = MenuItem.objects.filter(id__in=selected_items_ids)
        pedido = Pedido.objects.create(usuario=request.user)
        pedido.items.set(selected_items)
        pedido.save()
        # Llama a la tarea Celery de forma asíncrona
        process_order.delay(pedido.id)
        return redirect('order_success')

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/lista_pedidos.html'
    context_object_name = 'pedidos'
    paginate_by = 10  # Opcional: agrega paginación

    def test_func(self):
        return self.request.user.is_superuser  # Solo superusuarios pueden ver la lista
    
class OrderSuccessView(TemplateView):
    template_name = 'pedidos/order_success.html'

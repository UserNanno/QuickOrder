# urls.py en tu aplicación de pedidos

from django.urls import path
from .views import SubmitOrderView, OrderSuccessView
from .views import PedidoListView

urlpatterns = [
    path('submit_order/', SubmitOrderView.as_view(), name='submit_order'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    path('ver-pedidos/', PedidoListView.as_view(), name='ver-pedidos'),
]

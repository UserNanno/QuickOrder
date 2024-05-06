# urls.py en tu aplicación de menús

from django.urls import path
from .views import MenuListView, OrderSuccessView, SubmitOrderView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('menu/', MenuListView.as_view(), name='menu'),
    path('submit_order/', SubmitOrderView.as_view(),
         name='submit_order'),  # Agrega esta línea
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    # Asegúrate de que 'login' es el nombre correcto de tu URL de login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]

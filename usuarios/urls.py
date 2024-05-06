# urls.py
from django.urls import path
from .views import SignUpView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # Asegúrate de que el nombre 'login' coincide
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

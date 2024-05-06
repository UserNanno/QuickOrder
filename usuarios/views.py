# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    form_class = UserCreationForm
    # Redirige al usuario a la página de login después del registro
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()  # Guarda el nuevo usuario en la base de datos
        return super(SignUpView, self).form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Asegúrate que 'menu' corresponde a una URL definida en tus
        return reverse_lazy('menu')

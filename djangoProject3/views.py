from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import LoginForm, RegistrationForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    next_page = '/login'  # مسیری که کاربر پس از لاگ‌اوت به آن هدایت می‌شود


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = '/login'

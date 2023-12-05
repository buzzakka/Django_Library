from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterUserForm
from Catalog.models import Bookshelf


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('users:login'))


class ProfileUser(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_object(self, queryset=None):
        return self.request.user
from typing import Any
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterUserForm


class LoginUser(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    next_page = 'index'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}

    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)

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


class EditProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'image']
    template_name = 'users/edit_profile.html'
    extra_context = {'title': "Редактировать профиль"}
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self) -> str:
        return reverse_lazy('users:profile')
    
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


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

# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('users:login'))
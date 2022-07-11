from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .shortener import *
from .models import Urls


def home(request, token):
    long_url = Urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url, )


def make(request):
    form = UrlForm(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            a = Shortener().issue_token()
            new_url.short_url = a
            new_url.save()
        else:
            form = UrlForm()
            a = 'Invalid URL'
    return render(request, 'cutter/cutter.html', {'form': form, 'a': a})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'cutter/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'cutter/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

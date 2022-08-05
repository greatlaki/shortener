from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from .shortener import *
from .models import *


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


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


class ListLinks(ListView):
    model = Urls
    template_name = "cutter/links.html"
    context_object_name = "list_links_user"

    def get_user_context(self, **kwargs):
        user = get_object_or_404(
            User,
            username=self.kwargs.get('username')
        )

        links = Urls.objects.filter(author=user)

        context = {
            'list_links_user': links,
        }
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'cutter/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('list of links')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'cutter/login.html'

    def get_success_url(self):
        return reverse_lazy('list of links')


def logout_user(request):
    logout(request)
    return redirect('login')

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import *
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


def url_shortener(request):

    template = 'shorturl/shorten_url.html'
    context = {'form': ShorturlForm()}

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = ShorturlForm(request.POST)
        if used_form.is_valid() and request.user.is_authenticated:
            shortened_object = used_form.save(commit=False)
            shortened_object.author = request.user
            shortened_object.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        else:
            context['no_user'] = "Пожалуйста зарегистрируйтесь или войдите, чтобы использовать данную функцию "
        context['errors'] = used_form.errors

        return render(request, template, context)


def view_shorturl(request, shortened_part):
    """Redirect to the original link from shortened url"""
    try:
        shorturl = Urls.objects.get(short_url=shortened_part)
        shorturl.clicks += 1
        shorturl.save()
        return HttpResponseRedirect(shorturl.long_url)

    except Urls.DoesNotExist:
        raise Http404("Sorry, this link is broken.")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'cutter/login.html'

    def get_success_url(self):
        return reverse_lazy('list of links')


def logout_user(request):
    logout(request)
    return redirect('login')

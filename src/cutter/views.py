from django.shortcuts import render, redirect

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
    return render(request, 'cutter/base.html', {'form': form, 'a': a})

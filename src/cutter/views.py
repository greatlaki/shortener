from django.shortcuts import render, redirect
from django.urls import reverse

from cutter.service import shorten, load_url


def index(request):
    return render(request, 'cutter/index.html')


def redirect_hash(request, url_hash):
    original_url = load_url(url_hash).original_url
    return redirect(original_url)


def shorten_post(request):
    return shorten(request, request.POST['url'])


def shorten(request, url):
    shortened_url_hash = shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'cutter/link.html', {'shortened_url': shortened_url})

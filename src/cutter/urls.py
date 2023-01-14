from django.urls import path

from cutter.views import index, shorten_post, make_shorten, redirect_hash

urlpatterns = [
    path('', index, name='index'),
    path('shorten', shorten_post, name='shorten_post'),
    path('shorten/<str:url>', make_shorten, name='shorten'),
    path('<str:url_hash>', redirect_hash, name='redirect'),
]

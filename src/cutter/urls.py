from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', url_shortener, name='index'),
    path('view-urls/', view_urls, name='view_urls'),
    path('register/', register, name='register'),
    path('<str:shortened_part>', view_shorturl, name='shorturl'),
]

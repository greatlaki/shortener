from django.urls import path
from .views import *

urlpatterns = [
    path('<str:token>', home, name='home'),
    path('', make, name='Make new'),
    path('links/', ListLinks.as_view(), name='list of links'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]

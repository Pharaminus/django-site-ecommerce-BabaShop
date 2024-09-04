from django.urls import path, include
from django.contrib import admin
from shop.views import index, detail, validerAchat, confirmation

urlpatterns = [
    path('', index, name='home'),
    path('<int:myId>', detail, name='detail'),
    path('validerAchat', validerAchat, name='validerAchat'),
    path('confirmation', confirmation, name='confirmation')
]





from django.contrib import admin
from django.urls import path, include
from cart.views import cart


urlpatterns = [
    path("", cart, name="cart")
]

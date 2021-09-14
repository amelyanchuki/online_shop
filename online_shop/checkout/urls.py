from django.contrib import admin
from django.urls import path, include
from checkout.views import checkout

urlpatterns = [
    path("", checkout, name="checkout")
]

from django.contrib import admin
from django.urls import path, include
from single_product.views import single_product


urlpatterns = [
    path("", single_product, name="single_product")
]

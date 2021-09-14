from django.contrib import admin
from django.urls import path, include
from shop.views import shop_page


urlpatterns = [
    path("", shop_page, name="shop_page")
]

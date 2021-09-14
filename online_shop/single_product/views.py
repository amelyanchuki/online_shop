from django.shortcuts import render

def single_product(request):
    return render(request, "single_product.html", {})
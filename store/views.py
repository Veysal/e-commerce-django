from django.shortcuts import render,get_object_or_404
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.filter(is_available=True)[:8]
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail(request, product_slug):
    # get_object_or_404 либо находит объектб либо возвращает ошибку 404
    product = get_object_or_404(Product, slug = product_slug,is_available = True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
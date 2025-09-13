from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from django.db.models import Count, Q

# Create your views here.
def home(request):
    products = Product.objects.filter(is_available=True)[:8]
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail(request, product_slug):
    # get_object_or_404 либо находит объект либо возвращает ошибку 404
    product = get_object_or_404(Product, slug = product_slug,is_available = True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def category_list(request):
    categories = Category.objects.annotate(
        product_count = Count('products', filter=Q(products__is_available=True))
    ).order_by('-product_count', 'name')
    context = {'categories': categories}
    return render(request, "store/category_list.html", context)


def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter(category = category, is_available = True)
    context = {'category': category, 'products': products}
    return render(request, "store/product_list_by_category.html", context )

# get_object_or_404 - только для объектов
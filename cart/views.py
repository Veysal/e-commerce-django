from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# Новое представление для увеличения количества
@require_POST
def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

# Новое представление для уменьшения количества
@require_POST
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Получаем товар из сессии, чтобы проверить его количество
    item = cart.cart.get(str(product_id))

    if item:
        if item['quantity'] > 1:
            # Уменьшаем количество на 1
            cart.add(product=product, quantity=-1, update_quantity=False)
        else:
            # Если товар один, удаляем его
            cart.remove(product)
            
    return redirect('cart:cart_detail')

# Обновленное представление для страницы корзины
def cart_detail(request):
    cart = Cart(request)
    # Удаляем создание формы, она больше не нужна здесь
    return render(request, 'cart/detail.html', {'cart': cart})


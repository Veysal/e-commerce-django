from decimal import Decimal
from django.conf import settings
from store.models import Product

class Cart:
    # Инициализация корзины
    def __init__(self, request):
        self.session = request.session #Сессия
        cart = self.session.get(settings.CART_SESSION_ID) #Создаем экземпляр корзины
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if update_quantity: 
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True


    # Удаление товаров из корзины
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids).in_bulk()

        for product_id, item in self.cart.items():
            item_copy = item.copy()
            item_copy['product'] = products.get(int(product_id))
            item_copy['price'] = Decimal(item_copy['price'])
            item_copy['total_price'] = item_copy['price'] * item_copy['quantity']
            yield item_copy

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] 
                   for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()









        
from decimal import Decimal
from django.conf import settings
from store.models import Product, Category


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.product_price),
            }

        if update_quantity:
            self.cart[product_id] = quantity
        else:
            self.cart[product_id] += quantity

    def save(self):
        # Обновить сессию
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как измененный, чтобы сессия сохранилась
        self.session.modified = True

    def remove(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * Decimal(item['quantity'])

            yield item

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['total_price'] for item in self.cart.values())


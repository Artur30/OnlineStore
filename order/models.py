from django.db import models
from store.models import Product, Category


class Order(models.Model):
    order_first_name = models.CharField(verbose_name='First name', max_length=100)
    order_last_name = models.CharField(verbose_name='Last name', max_length=100)
    order_email = models.EmailField(verbose_name='Email')
    order_address = models.CharField(verbose_name='Address', max_length=300)
    order_postal_code = models.CharField(verbose_name='Postal code', max_length=20)
    order_city = models.CharField(verbose_name='City', max_length=50)
    order_created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    order_updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    order_paid = models.BooleanField(verbose_name='Paid', default=False)

    class Meta:
        db_table = 'order'
        ordering = ('-order_created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return 'Order {id}'.format(id=self.id)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order_item_order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    order_item_product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    order_item_price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    order_item_quantity = models.PositiveIntegerField(verbose_name='Quantity', default=1)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.order_item_price * self.order_item_quantity



from django.contrib import admin
from order.models import OrderItem, Order


class OrderInLine(admin.StackedInline):
    model = OrderItem
    raw_id_fields = ['order_item_product']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInLine]
    list_display = [
        'id', 'order_first_name', 'order_last_name', 'order_email', 'order_address', 'order_postal_code',
        'order_city', 'order_created', 'order_updated', 'order_paid',
    ]
    list_filter = ['order_paid', 'order_created', 'order_updated']


admin.site.register(Order, OrderAdmin)



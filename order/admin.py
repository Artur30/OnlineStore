from django.contrib import admin
from order.models import OrderItem, Order
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(model_admin, request, queryset):
    opts = model_admin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


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
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)



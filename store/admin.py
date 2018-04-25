from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug')
    prepopulated_fields = {'category_slug': ('category_name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_slug', 'product_price', 'product_stock',
                    'product_available', 'product_created', 'product_updated')
    list_filter = ('product_available', 'product_created', 'product_updated')
    prepopulated_fields = {'product_slug': ('product_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)



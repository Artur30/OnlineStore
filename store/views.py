from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


def product_list(request):
    products = Product.objects.filter(product_available=True)
    context = {'products': products}
    return render(request, 'store/product/list.html', context)


def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, category_slug=category_slug)
    products = Product.objects.filter(category=category)

    context = {'products': products}
    return render(request, 'store/product/list.html', context)


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product,
                                id=id, product_slug=product_slug,
                                product_available=True)
    context = {'product': product}
    return render(request, 'store/product/detail.html', context)


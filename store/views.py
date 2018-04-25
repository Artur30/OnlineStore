from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


def product_list(request, category_slug=None):
    args = dict()
    args['category'] = None
    args['products'] = Product.objects.filter(product_available=True)

    if category_slug:
        args['category'] = get_object_or_404(Category, category_slug=category_slug)
        args['products'] = Product.objects.filter(category=args['category'])

    return render(request, 'store/product/list.html', args)


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product,
                                id=id, product_slug=product_slug,
                                product_available=True)
    context = {'product': product}
    return render(request, 'store/product/detail.html', context)

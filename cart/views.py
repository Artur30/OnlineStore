from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, Category
from cart.cart import Cart
from cart.forms import CartAddProductForm


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.POST:
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cart.add(
                product=product,
                quantity=form.cleaned_data['quantity'],
                update_quantity=form.cleaned_data['update'],
            )
        return redirect('cart:cart_detail')
    #return render(request, '', {''})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})







from django.shortcuts import render
from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from django.template.context_processors import csrf
from order.tasks import order_created


def order_create(request):
    args = {}
    args.update(csrf(request))
    args['cart'] = Cart(request)

    if request.POST:
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            args['order'] = form.save()
            for item in args['cart']:
                OrderItem.objects.create(
                    order_item_order=args['order'],
                    order_item_product=item['product'],
                    order_item_price=item['price'],
                    order_item_quantity=item['quantity']
                )
            args['cart'].clear()
            order_created.delay(args['order'].id)
            return render(request, 'order/created.html', args)
    else:
        args['form'] = OrderCreateForm
    return render(request, 'order/create.html', args)


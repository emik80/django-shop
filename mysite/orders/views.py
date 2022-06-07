from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_cost = cart.get_total_price()
            order.user_id = request.user.id
            order.email = request.user.email
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


@csrf_exempt
def fondy_callback(request):
    data = request.POST
    if 'payment_id' in data:
        payment_id = data['payment_id']
        order_id = data['merchant_data'].split(',')[2].split(':')[-1].strip('"')

        order = get_object_or_404(Order, id=order_id)
        order.paid = True
        order.payment_id = payment_id
        order.save()

    return redirect('shop:account')

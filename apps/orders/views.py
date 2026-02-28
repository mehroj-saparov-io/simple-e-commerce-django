from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.cart.utils import get_cart, clear_cart
from apps.products.models import Product
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = get_cart(request)
    if not cart:
        return redirect('product_list')

    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0

    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        # Create Order
        order = Order.objects.create(user=request.user, total_price=total)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price,
                subtotal=item['subtotal'],
            )
        clear_cart(request)
        return redirect('order_success', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total': total})
    
@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})
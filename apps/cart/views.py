from django.shortcuts import render, redirect, get_object_or_404
from apps.products.models import Product
from .utils import add_to_cart, remove_from_cart, get_cart, update_cart

from django.views.decorators.http import require_POST


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_remove(request, product_id):
    remove_from_cart(request, product_id)
    return redirect('cart_detail')

@require_POST
def cart_update(request, product_id):
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1
    update_cart(request, product_id, quantity)
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_cart(request)
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
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})
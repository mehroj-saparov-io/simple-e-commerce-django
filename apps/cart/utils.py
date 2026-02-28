SESSION_CART_KEY = 'cart'

def get_cart(request):
    return request.session.get(SESSION_CART_KEY, {})

def save_cart(request, cart):
    request.session[SESSION_CART_KEY] = cart
    request.session.modified = True

def add_to_cart(request, product_id, quantity=1):
    cart = get_cart(request)
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity
    save_cart(request, cart)

def remove_from_cart(request, product_id):
    cart = get_cart(request)
    cart.pop(str(product_id), None)
    save_cart(request, cart)
    
def update_cart(request, product_id, quantity):
    cart = get_cart(request)
    if quantity <= 0:
        cart.pop(str(product_id), None)
    else:
        cart[str(product_id)] = quantity
    save_cart(request, cart)

def clear_cart(request):
    save_cart(request, {})
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    featured_products = Product.objects.order_by('-id')[:6]  # oxirgi 6 ta product
    context = {
        'featured_products': featured_products,
    }
    return render(request, 'home.html', context)


@login_required
def product_list(request):
    products = Product.objects.filter(available=True)

    # 🔍 SEARCH
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # 💰 PRICE FILTER
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    try:
        if min_price:
            min_price_val = float(min_price)
            products = products.filter(price__gte=min_price_val)
    except ValueError:
        pass

    try:
        if max_price:
            max_price_val = float(max_price)
            products = products.filter(price__lte=max_price_val)
    except ValueError:
        pass

    # 📄 PAGINATION
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'products/product_list.html', context)


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
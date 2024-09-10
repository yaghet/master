from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import Group
from .models import Product, Order


def shop_view(request: HttpRequest):
    products = [
        ('desktop', 1999),
        ('laptop', 1999),
        ('smartphone', 999),
    ]
    context_shop = {
        'products': products,
    }
    return render(request, 'shopapp/shop-app.html', context=context_shop)


def group_list(request: HttpRequest):
    context_group = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context_group)


def products_list(request: HttpRequest):
    context_product = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context_product)


def orders_list(request: HttpRequest):
    context_orders ={
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context_orders)
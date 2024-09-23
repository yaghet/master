from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import Group
from .models import Product, Order
from .forms import ProductForm, OrderForm

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

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:products_list')
            return redirect(url)
    else:
        form = ProductForm()
    context_create_product = {
        'form': form,
    }
    return render(request, 'shopapp/create-product.html', context=context_create_product)


def orders_list(request: HttpRequest):
    context_orders ={
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context_orders)


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:orders_list')
            return redirect(url)
    else:
        form = OrderForm()

    context_create_order = {
        'form': form,
    }
    return render(request, 'shopapp/create-order.html', context=context_create_order)

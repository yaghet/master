from django.urls import path
from .views import shop_view, group_list, products_list, orders_list, create_product, create_order

app_name = 'shopapp'

urlpatterns = [
    path('', shop_view, name='index'),
    path('groups/', group_list, name='groups_list'),
    path('products/', products_list, name='products_list'),
    path('orders/', orders_list, name='orders_list'),
    path('create/', create_product, name='create_product'),
    path('orders/create_order/', create_order, name='create_order'),
]

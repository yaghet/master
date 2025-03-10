from django.urls import path
from .views import (
    ShopAppView,
    GroupListView,
    CreateProductView,
    ProductsListView,
    ProductsDetailsView,
    ProductUpdateView,
    ProductDeleteView,
    OrdersListView,
    OrdersDetailView,
    CreateOrderView,
    OrderUpdateView,
    OrderDeleteView,
    OrderExportView,
)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopAppView.as_view(), name='index'),
    path('groups/', GroupListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', CreateProductView.as_view(), name='products_create'),

    path('products/<int:pk>/', ProductsDetailsView.as_view(), name='products_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrdersDetailView.as_view(), name='orders_details'),

    path('orders/create_order/', CreateOrderView.as_view(), name='create_orders'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/export/', OrderExportView.as_view(), name='export_orders'),
]
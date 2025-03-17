from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (OrderDataExportView, OrderDetailView, ProductCreateView,
                    ProductDeleteView, ProductDetailsView,
                    ProductsDataExportView, ProductsListView,
                    ProductUpdateView, ProductViewSet, ShopIndexView,
                    UserOrdersListView)

app_name = "shopapp"

routers = DefaultRouter()
routers.register("products", ProductViewSet)

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("api/", include(routers.urls)),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/export/", ProductsDataExportView.as_view(), name="products-export"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="user_orders_product"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),

    path("users/<int:pk>/orders/", UserOrdersListView.as_view(), name="orders_list"),
    path("users/<int:user_id>/orders/export/",  OrderDataExportView.as_view(), name="orders-export"),
]

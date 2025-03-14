from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (OrderDetailView, OrdersListView, ProductCreateView,
                    ProductDeleteView, ProductDetailsView,
                    ProductsDataExportView, ProductsListView,
                    ProductUpdateView, ProductViewSet, ShopIndexView,
                    LatestProductsFeedView,)

app_name = "shopapp"

routers = DefaultRouter()
routers.register("products", ProductViewSet)

urlpatterns = [
    path('products/latest/feed/', LatestProductsFeedView(), name='latest-products-feed'),
    path("", ShopIndexView.as_view(), name="index"),
    path("api/", include(routers.urls)),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/export/", ProductsDataExportView.as_view(), name="products-export"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
]

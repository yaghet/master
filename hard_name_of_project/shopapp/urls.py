from django.urls import path
from .views import shop_app


app_name = 'shopapp'
urlpatterns = [
    path('', shop_app, name='index')
]
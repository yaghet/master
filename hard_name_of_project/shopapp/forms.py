from django import forms
from .models import Product, Order
from django.contrib.auth.models import Group

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount', 'archive'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
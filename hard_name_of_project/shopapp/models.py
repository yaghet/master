from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    objects = None

    class Meta:
        ordering = ['name', 'price']

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True)
    archive = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'Product pk={self.pk} name={self.name!r}'


class Order(models.Model):
    objects = None
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')
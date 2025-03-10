from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


def product_preview_directory_path(instance: 'Product', filename: str) -> str:

    """

    Функция для генерации 'path' в корневой папке директории для хранения 'preview' продукта

    """

    return 'products/product_{pk}/preview/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:

    """

    Функция для генерации 'path' в корневой папке директории для хранения 'images' продукта

    """

    return 'products/product_{pk}/images/{filename}'.format(
        pk=instance.product.pk,
        filename=filename,
    )


class Product(models.Model):

    objects = None

    class Meta:
        ordering = ['name', 'price']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True)
    archive = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path)


    def __str__(self) -> str:
        return f'Product pk={self.pk} name={self.name!r}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_images_directory_path)
    description = models.TextField(max_length=200, null=False, blank=True)


class Order(models.Model):
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    objects = None

    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')
    receipt = models.FileField(null=True, upload_to='orders/receipts/')
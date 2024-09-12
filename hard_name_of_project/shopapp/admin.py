from django.contrib import admin
from .models import Product, Order
from django.http import HttpRequest
from django.db.models import QuerySet
from .admin_mixins import ExportAsCSCMixin


class OrderInline(admin.TabularInline):
    model = Product.orders.through
    extra = 0


@admin.action(description='Archive Products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=True)


@admin.action(description='Unarchive Products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSCMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'archive'
    list_display_links = 'pk', 'name'
    ordering = '-name',
    search_fields = 'name', 'description', 'price'
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('price_options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide'),
        }),
        ('extra_options', {
            'fields': ('archive',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archive" is for soft delete',
        }),
    ]

    @staticmethod
    def description_short(obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


class ProductInline(admin.StackedInline):
    model = Order.products.through
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'delivery_address', 'promocode', 'create_at', 'user_verbose'
    search_fields = 'delivery_address', 'create_at'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    @staticmethod
    def user_verbose(obj: Order) -> str:
        return obj.user.first_name or obj.user.username

from csv import DictReader
from io import TextIOWrapper

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import path

from .admin_mixins import ExportAsCSVMixin
from .forms import CsvImportForm
from .models import Order, Product, ProductImage, User


class OrderInline(admin.TabularInline):
    model = Product.orders.through


class ProductInline(admin.StackedInline):
    model = ProductImage


@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
        ProductInline,
    ]
    # list_display = "pk", "name", "description", "price", "discount"
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = "-name", "pk"
    search_fields = "name", "description"
    fieldsets = [
        (None, {
           "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse"),
        }),
        ("Images", {
            "fields": ("preview", ),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


# admin.site.register(Product, ProductAdmin)


# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    change_list_template = "shopapp/order_change_list.html"
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode", "created_at", "user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

    def import_csv(self, request: HttpRequest) -> HttpResponse:

        if request.method == "GET":
            form = CsvImportForm()
            context = {"form": form}
            return render(request, 'admin/csv_form.html', context)

        form = CsvImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {"form": form}
            return render(request, 'admin/csv_form.html', context, status=400)

        csv_file = TextIOWrapper(
            form.files['csv_file'].file,
            encoding=request.encoding,
        )
        reader = DictReader(csv_file)

        orders_to_create = []
        for row in reader:
            user_id = row.pop('user')
            user_instance = User.objects.get(id=user_id)
            row['user'] = user_instance

            product_id = row.pop('products')
            product = Product.objects.get(id=product_id)

            order = Order(**row)
            orders_to_create.append((order, product))


        if orders_to_create:
            orders = [order for order, _ in orders_to_create]
            Order.objects.bulk_create(orders)

            for order, product in orders_to_create:
                order.products.add(product)

        self.message_user(request, "Successfully imported orders.")

        return redirect("..")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import_csv/', self.import_csv, name="import_order_csv"),
        ]
        return new_urls + urls
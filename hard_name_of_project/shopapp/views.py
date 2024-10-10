from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.models import Group
from .models import Product, Order
from .forms import GroupForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# View для отображения продуктов
class ShopAppView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ("desktop", 1999),
            ("laptop", 1999),
            ("smartphone", 999),
        ]
        context_shop = {
            "products": products,
        }
        return render(request, "shopapp/shop-app.html", context=context_shop)


# View для отображения списка групп
class GroupListView(View):
    def get(self, request: HttpRequest):
        context_group = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related("permissions").all(),
        }
        return render(request, "shopapp/groups-list.html", context=context_group)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# View для отображения списка продуктов
class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archive=False)


# View для отображения деталей выбранного продукта
class ProductsDetailsView(DetailView):
    template_name = "shopapp/product-details.html"
    model = Product
    context_object_name = "product"


# View для создания продукта
class CreateProductView(PermissionRequiredMixin, CreateView):

    permission_required = "shopapp.add_product"

    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


# View для обновления продукта
class ProductUpdateView(UserPassesTestMixin, UpdateView):

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        self.object = self.get_object()

        has_edit_perm = self.request.user.has_perm("shopapp.change_product")
        created_by_current_user = self.object.created_by == self.request.user

        return has_edit_perm and created_by_current_user

    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:products_details",
            kwargs={"pk": self.object.pk},
        )


# View для выполнения архивации выбранной сущности
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


# View для отображения списка заказов
class OrdersListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.select_related("user").prefetch_related("products")


# View для отображения деталей выбранного заказа
class OrdersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = Order.objects.select_related("user").prefetch_related("products")


# View для создания заказа
class CreateOrderView(CreateView):
    model = Order
    fields = "user", "products", "delivery_address", "promocode"
    success_url = reverse_lazy("shopapp:orders_list")


# View для обновления заказа
class OrderUpdateView(UpdateView):
    model = Order
    fields = "user", "products", "promocode", "delivery_address"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:orders_details", kwargs={"pk": self.object.pk})


# View для полного удаления выбранной сущности
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders_list")


class OrderExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        orders = Order.objects.order_by("pk").all()
        orders_data = {"orders": [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user.pk,
                "products": [product.pk for product in order.products.all()]
            }
                for order in orders
                    ]
            }

        return JsonResponse(orders_data)

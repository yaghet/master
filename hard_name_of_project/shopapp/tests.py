from django.test import TestCase
from django.urls import reverse
from shopapp.models import Order
from django.contrib.auth.models import User, Permission



class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='Not_Admin', password='default')
        cls.user.user_permissions.add(Permission.objects.get(codename='view_order'))

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)
        self.order_name = Order.objects.create(
            delivery_address='Russia',
            promocode="Skillbox",
            user_id=self.user.pk,
        )

    def tearDown(self):
        self.order_name.delete()

    def test_order_details(self):
        response = self.client.get(
            reverse('shopapp:orders_details', kwargs={"pk": self.order_name.pk}),
        )
        self.assertContains(response, 'Russia' and 'Skillbox', count=1)
        self.assertTrue(response.context.get('order').pk == 1)


class OrderExportViewTestCase(TestCase):

    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
        'orders-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Skillbox', password='default')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_order_export(self):

        response = self.client.get(reverse('shopapp:export_orders'))
        self.assertTrue(response.status_code == 200)

        orders = Order.objects.order_by('pk').all()

        expected_data = {"orders": [
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

        self.assertEqual(response.json(), expected_data)
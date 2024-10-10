from django.test import TestCase, Client
from django.urls import reverse


class GetCookieViewTest(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse("myauth:cookie-get"))
        self.assertContains(response, 'Cookie')


class FooBarViewTest(TestCase):

    def test_foobar(self):
        response = self.client.get(reverse('myauth:foobar'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers['content-type'], 'application/json'
        )
        expected_date = {"one": "True", "zero": "False"}
        self.assertJSONEqual(response.content, expected_date)
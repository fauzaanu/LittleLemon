from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title="Tomato Soup", price = 9.90, inventory = 4)
        MenuItem.objects.create(title="Pasta Bolognese", price = 13.90, inventory = 6)

        self.client = APIClient()

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        menu = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        print("Response Data:", response.data)
        print("Serializer Data:", serializer.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], serializer.data)
from django.test import TestCase

from restaurant.models import MenuItem


class MenuTest(TestCase):
    def test_menu_item_get_item(self):
        item = MenuItem.objects.create(title='Pasta', price=12.99, inventory=10)
        self.assertEqual(item, 'Pasta : 12.99')


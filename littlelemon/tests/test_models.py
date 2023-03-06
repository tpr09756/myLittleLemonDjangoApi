from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Tanjia",
            price=15.99,
            inventory=4
        )
        self.assertEqual(str(item), "Tanjia : 15.99")
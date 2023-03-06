from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer

mocks = [
    {
        'title' : 'Couscous',
        'price' : 25.49,
        'inventory' : 5,
    },
    {
        'title' : 'Tajine',
        'price' : 17.99,
        'inventory' : 4,
    },
    {
        'title' : 'Tanjia',
        'price' : 15.99,
        'inventory' : 4,
    },
]

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for mock in mocks:
            Menu.objects.create(
                title=mock['title'],
                price=mock['price'],
                inventory=mock['inventory']
            )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
from django.test import TestCase
from .models import Menu

class MenuTestCase(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(name="Pizza", price=12.50)
        self.assertEqual(item.name, "Pizza")

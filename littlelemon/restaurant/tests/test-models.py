from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_menu_str_representation(self):
        # Create a Menu instance
        menu_item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)

        # Define the expected string representation with the correct format
        expected_str = "IceCream : 80.00"

        # Check if the actual string representation matches the expected value
        self.assertEqual(str(menu_item), expected_str)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemsViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title="Dish1", price=10.50, inventory=50)
        Menu.objects.create(title="Dish2", price=15.75, inventory=30)

        # Set up the client for making API requests
        self.client = APIClient()

    def test_get_all_menu_items(self):
        # Get the URL for the MenuItemsView using reverse
        url = reverse('menuitem-list')

        # Make a GET request to retrieve all menu items
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve the expected serialized data for all menu items
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data in the response equals the expected data
        self.assertEqual(response.data, expected_data)

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from .models import *


class BookingViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all_bookings(self):
        # Create some test data
        booking.objects.create(tableno=1, persons=4)
        booking.objects.create(tableno=2, persons=2)
        booking.objects.create(tableno=3, persons=6)

        # Make a GET request to the bookingView
        response = self.client.get(reverse('booking-list'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data is the expected length
        self.assertEqual(len(response.data), 3)

class MenuViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all_menu_items(self):
        # Create some test data
        menu.objects.create(item='Burger', price=10)
        menu.objects.create(item='Fries', price=5)
        menu.objects.create(item='Drink', price=2)

        # Make a GET request to the menuView
        response = self.client.get(reverse('menu-list'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data is the expected length
        self.assertEqual(len(response.data), 3)

class SingleMenuItemViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = menu.objects.create(item='Burger', price=10)

    def test_get_single_menu_item(self):
        # Make a GET request to the SingleMenuItemView
        response = self.client.get(reverse('menu-detail', args=[self.item.pk]))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data is the expected item
        self.assertEqual(response.data['item'], 'Burger')
        self.assertEqual(response.data['price'], 10)

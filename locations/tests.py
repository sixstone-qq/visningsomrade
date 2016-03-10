from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch


from .models import Location


class LocationTests(TestCase):

    def test_str(self):
        """Test string representation of the Location object"""
        l = Location(lat=1.1, lon=1.1)
        self.assertEqual(str(l), "(1.1, 1.1)")
        l.address = "Nice address"
        self.assertEqual(str(l), "(1.1, 1.1) Nice address")


class LocationAPITests(APITestCase):

    @patch('locations.fusiontables.LocationFTService')
    def test_empty(self, mock_class):
        """Test creation and empty a list of addresses"""
        url = reverse('locations:location-list')
        loc_data = {'lat': 2.2, 'lon': 2.2, 'address': 'Nice one'}
        response = self.client.post(url, loc_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        # New addr
        loc_data['lat'] = 2.3
        loc_data['address'] = 'Another nice one'
        response = self.client.post(url, loc_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 2)

        # Empty data
        empty_url = reverse('locations:location-empty')
        response = self.client.post(empty_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Location.objects.count(), 0)

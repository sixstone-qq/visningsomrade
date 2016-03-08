from django.test import TestCase

from .models import Location


class LocationTests(TestCase):

    def test_str(self):
        """Test string representation of the Location object"""
        l = Location(lat=1.1, lon=1.1)
        self.assertEqual(str(l), "(1.1, 1.1)")
        l.address = "Nice address"
        self.assertEqual(str(l), "(1.1, 1.1) Nice address")

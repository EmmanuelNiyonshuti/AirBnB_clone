#!/usr/bin/python3
"""
This module comprises the tests for the Place subclass
of the base model classo
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_city_id_attr(self):
        """
        Test case to verify the city_id attribute of the Place class.
        """
        self.assertEqual(Place.city_id, "")

    def test_name_attr(self):
        """
        Test case to verify the name attribute of the Place class.
        """
        self.assertEqual(Place.name, "")

    def test_user_id_attr(self):
        """
        Test case to verify the user_id attribute of the Place class.
        """
        self.assertEqual(Place.user_id, "")

    def test_description_attr(self):
        """
        Test case to verify the description attribute of the Place class.
        """
        self.assertEqual(Place.description, "")

    def test_number_rooms_attr(self):
        """
        Test case to verify the number_rooms attribute of the Place class.
        """
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """
        Test case to verify the number_bathrooms attribute of the Place class.
        """
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guests_attr(self):
        """
        Test case to verify the max_guest attribute of the Place class.
        """
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night_attr(self):
        """
        Test case to verify the price_by_night attribute of the Place class.
        """
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_attr(self):
        """
        Test case to verify the latitude attribute of the Place class.
        """
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude_attr(self):
        """
        Test case to verify the longitude attribute of the Place class.
        """
        self.assertEqual(Place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """
        Test case to verify the amenity_ids attribute of the Place class.
        """
        self.assertEqual(Place.amenity_ids, [])

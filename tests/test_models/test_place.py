#!/usr/bin/python3
"""Tests City object"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_city_id_attr(self):
        self.assertEqual(Place.city_id, "")
    def test_name_attr(self):
        self.assertEqual(Place.name, "")
    def test_user_id_attr(self):
        self.assertEqual(Place.user_id, "")
    def test_description_attr(self):
        self.assertEqual(Place.description, "")
    def test_number_rooms_attr(self):
        self.assertEqual(Place.number_rooms, 0)
    def test_number_bathrooms_attr(self):
        self.assertEqual(Place.number_bathrooms, 0)
    def test_max_guests_attr(self):
        self.assertEqual(Place.max_guest, 0)
    def test_price_by_night_attr(self):
        self.assertEqual(Place.price_by_night, 0)
    def test_latitude_attr(self):
        self.assertEqual(Place.latitude, 0.0)
    def test_longitude_attr(self):
        self.assertEqual(Place.longitude, 0.0)
    def test_amenity_ids_attr(self):
        self.assertEqual(Place.amenity_ids, [])
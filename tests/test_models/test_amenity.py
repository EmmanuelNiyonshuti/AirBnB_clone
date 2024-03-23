#!/usr/bin/python3
"""Tests City object"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_place_id_attr(self):
        self.assertEqual(Amenity.name, "")
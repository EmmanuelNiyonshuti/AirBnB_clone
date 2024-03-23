#!/usr/bin/python3
"""Tests City object"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_id_attr(self):
        self.assertEqual(City.State_id, "")
    def test_name_attr(self):
        self.assertEqual(City.name, "")
#!/usr/bin/python3
"""
This module comprises tests for City subclass
of base model class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """
    def test_city_id_attr(self):
        """
        Test case to verify the State_id attribute of the City class.
        """
        self.assertEqual(City.State_id, "")

    def test_name_attr(self):
        """
        Test case to verify the name attribute of the City class.
        """
        self.assertEqual(City.name, "")

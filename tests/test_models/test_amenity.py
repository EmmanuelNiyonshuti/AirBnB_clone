#!/usr/bin/python3
"""
This module comprises tests for a Amenity subclass
of basemodel class.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """
    def test_name_attr(self):
        """
        Test case to verify the name attribute of Amenity class.
        """
        self.assertEqual(Amenity.name, "")

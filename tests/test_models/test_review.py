#!/usr/bin/python3
"""
This model contains the tests for the Review subclass of the base model.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """
    def test_place_id_attr(self):
        """
        Test case to verify the place_id attribute of the Review class.
        """
        self.assertEqual(Review.place_id, "")

    def test_user_id_attr(self):
        """
        Test case to verify the user_id attribute of the Review class.
        """
        self.assertEqual(Review.user_id, "")

    def test_text_attr(self):
        """
        Test case to verify the text attribute of the Review class.
        """
        self.assertEqual(Review.text, "")

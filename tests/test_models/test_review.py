#!/usr/bin/python3
"""Tests City object"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_place_id_attr(self):
        self.assertEqual(Review.place_id, "")
    def test_user_id_attr(self):
        self.assertEqual(Review.user_id, "")
    def test_text_attr(self):
        self.assertEqual(Review.text, "")
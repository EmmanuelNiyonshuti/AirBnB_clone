#!/usr/bin/python3
"""Tests City object"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_email_attr(self):
        self.assertEqual(User.email, "")
    def test_password_attr(self):
        self.assertEqual(User.password, "")
    def test_first_name_attr(self):
        self.assertEqual(User.first_name, "")
    def test_last_name_attr(self):
        self.assertEqual(User.last_name, "")

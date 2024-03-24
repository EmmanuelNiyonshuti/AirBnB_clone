#!/usr/bin/python3
"""
This module contains the tests for the User sub class of
the base model class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """
    def test_email_attr(self):
        """
        Test case to verify the email attribute of the User class.
        """
        self.assertEqual(User.email, "")

    def test_password_attr(self):
        """
        Test case to verify the password attribute of the User class.
        """
        self.assertEqual(User.password, "")

    def test_first_name_attr(self):
        """
        Test case to verify the first_name attribute of the User class.
        """
        self.assertEqual(User.first_name, "")

    def test_last_name_attr(self):
        """
        Test case to verify the last_name attribute of the User class.
        """
        self.assertEqual(User.last_name, "")

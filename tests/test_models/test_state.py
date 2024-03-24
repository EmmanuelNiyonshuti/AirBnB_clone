#!/usr/bin/python3
"""
This module comprises tests for a State subclass
of basemodel class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """
    def test_name_attr(self):
        """
        Test case to verify the name attribute of State class.
        """
        self.assertEqual(State.name, "")
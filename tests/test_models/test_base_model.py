#!/usr/bin/python3
"""
This module contains tests for the base module class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Initialize a BaseModel object before each test method.
        """
        self.model = BaseModel()
        self.model.name = "My_First_Model"
        self.model.my_number = 89

    def test_id_existence(self):
        """
        Test if the 'id' attribute exists in the BaseModel instance.
        """
        self.assertTrue(hasattr(self.model, 'id'))

    def test_id_generation(self):
        """
        Test if the 'id' attribute is generated as a string.
        """
        self.assertTrue(isinstance(self.model.id, str))

    def test_created_at_existence(self):
        """
        Test if the 'created_at' attribute exists in the BaseModel instance.
        """
        self.assertTrue(hasattr(self.model, 'created_at'))

    def test_created_at_type(self):
        """
        Test if the 'created_at' attribute is of type datetime.
        """
        self.assertTrue(isinstance(self.model.created_at, datetime))

    def test_updated_at_existence(self):
        """
        Test if the 'updated_at' attribute exists in the BaseModel instance.
        """
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_updated_at_type(self):
        """
        Test if the 'updated_at' attribute is of type datetime.
        """
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        expctd_output = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expctd_output)

    def test_save_method(self):
        """
        Test if the 'save' method updates the 'updated_at' attribute.
        """
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test the 'to_dict' method of the BaseModel class.
        """
        model_dict = self.model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

        # Check if created_at and updated_at are in ISO format
        self.assertTrue(isinstance(datetime.fromisoformat(model_dict['created_at']), datetime))
        self.assertTrue(isinstance(datetime.fromisoformat(model_dict['updated_at']), datetime))

    def test_json_serialization(self):
        """
        Test if the output of 'to_dict' method can be serialized into JSON.
        """
        model_json = self.model.to_dict()
        json_str = json.dumps(model_json)
        self.assertTrue(isinstance(json_str, str))

    def test_create_instance_from_dict(self):
        """
        Test if a BaseModel instance can be created
        from a dictionary representation.
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_create_instance_from_empty_dict(self):
        """
        Test if a BaseModel instance can be created from an empty dictionary.
        """
        new_model = BaseModel({})
        self.assertIsNotNone(new_model.id)
        self.assertIsNotNone(new_model.created_at)
        self.assertIsNotNone(new_model.updated_at)

        # Check if created_at and updated_at are datetime objects
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

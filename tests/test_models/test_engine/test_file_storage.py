#!/usr/bin/python3
"""
This module contains tests for for my FileStorage class using unittest.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up method to create an instance of FileStorage.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tear down method to reset __objects and
        remove the file after each test.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_file_path_default_value(self):
        """
        Test if the default value of __file_path is correct.
        """
        self.assertEqual("file.json", FileStorage._FileStorage__file_path)

    def test_objects_default_value(self):
        """
        Test if the default value of __objects is an empty dictionary.
        """
        self.assertEqual({}, FileStorage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """
        Test reloading when the file does not exist.
        """
        self.storage.reload()
        self.assertEqual({}, self.storage.all())

    def test_new(self):
        """
        Test new() method to add a new object to __objects.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual({"BaseModel." + obj.id: obj}, self.storage.all())

    def test_save(self):
        """
        Test save() method to save __objects to a JSON file.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("BaseModel." + obj.id, data)
        self.assertEqual(obj.to_dict(), data["BaseModel." + obj.id])

    def test_reload_existing_file(self):
        """
        Test reloading when the file exists and contains data.
        """
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel()
        obj2.save()

        self.storage.reload()
        self.assertIn("BaseModel." + obj1.id, self.storage.all())
        self.assertIn("BaseModel." + obj2.id, self.storage.all())

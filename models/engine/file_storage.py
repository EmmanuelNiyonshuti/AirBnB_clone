#!/usr/bin/python3
"""
This module complises File strorage class
File storage class consist of methods and attributes
designed to handle serialization
and deserialization of instances
of the classes.
"""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file back to instances
    """

    __file_path, __objects = "file.json", {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new objects to __objects dictionary.

        Args:
            obj: The object to be added.
        """

        special_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[special_key] = obj

    def save(self):
        """
        Saves __objects dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, "a", encoding="utf-8") as json_f:
            my_dict = {k: v.to_dict()for k, v in FileStorage.__objects.items()}
            json.dump(my_dict, json_f)

    def reload(self):
        """
        Loads objects from JSON file into __objects dictionary.
        """
        if not os.path.exists(self.__file_path):
            return

        with open(FileStorage.__file_path, "a", encoding="utf-8") as json_f:
            serialized_data = json.load(json_f)
        objects = {}
        for id, data in serialized_data.items():
            class_name = data["__class__"]
            obj_class = self.all_classes()[class_name]
            objects[id] = obj_class(**data)
            FileStorage.__objects = objects

    def all_classes(self):
        """
        Helper method
        Returns a dictionary mapping class names to their actual class objects.
        """
        return{
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def obj_attr(self):
        """
        Helper Method
        Returns a nested dictionary  of class names with the dictionary
        of their attributes mapping to their types accordingly.
        """
        return
    {
        "BaseModel":
        {
            "id": str,
            "created_at": datetime.datetime,
            "updated_at": datetime.datetime
        },
        "User":
        {
            "email": str,
            "password": str,
            "first_name": str,
            "last_name": str
        },
        "Place":
        {
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": []
        },
        "State":
        {
            "name": str
        },
        "City":
        {
            "state_id": str,
            "name": str
        },
        "Review":
        {
            "place_id": str,
            "user_id": str,
            "text": str
        },
        "Amenity":
        {
            "name": str
        }
    }

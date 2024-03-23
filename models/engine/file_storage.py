#!/usr/bin/python3
import json
import os
import datetime
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
            with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
                my_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
                json.dump(my_dict, json_f, indent=4)

        def reload(self):
            """
            Loads objects from JSON file into __objects dictionary.
            """
            if not os.path.exists(FileStorage.__file_path):
                return
            try:
                    with open(FileStorage.__file_path, "r", encoding="utf-8") as json_file:
                        loaded_data = json.load(json_file)
                    loaded_objs = {}
                    for obj_id, obj_data in loaded_data.items():
                        class_name = obj_data["__class__"]
                        obj_class = self.all_classes()[class_name]
                        loaded_objs[obj_id] = obj_class(**obj_data)
                    FileStorage.__objects = loaded_objs
            except json.JSONDecodeError:
                 pass

        def all_classes(self):
            from models.base_model import BaseModel
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
            "Returns all cls attributes mapping to their corresponding types"
            return{
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
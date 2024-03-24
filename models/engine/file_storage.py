#!/usr/bin/python3
"""
This module complises File strorage class
File storage class consist of methods and attributes
designed to handle serialization
and deserialization of instances
of the classes.
"""
import json
import os


class FileStorage:
    """
    This class performs serialization and deserialization of Python instances.
    """
    __file_path, __objects = "file.json", {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
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
        Serialize _objects and saves it to a json file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            obj = {}
            for k, v in FileStorage.__objects.items():
                obj[k] = v.to_dict()
            json.dump(obj, json_f)

    def reload(self):
        """
        Deserialize JSON file into __objects only if the JSOn file exists.
        Otherwise it does nothing.
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, encoding="utf-8") as json_f:
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
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        return{
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

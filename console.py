#!/usr/bin/python3
"""
This module comprises the entry point of the My console.
"""
import cmd
import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is the entry point of the console application.
    It provides functionalities for managing instances of various classes
    and interacts with the storage system.
    """
    _attrs = {
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

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Handles End-Of-File (EOF) to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing when an empty line is entered
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of a specified class.
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.all_classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Displays the string representation of an instance.
        """
        if line is None or line == "":
            print("** class name missing **")
        else:
            arg = line.split(' ')
            if arg[0] not in storage.all_classes():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                if f"{arg[0]}.{arg[1]}" not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[f"{arg[0]}.{arg[1]}"])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Saves the changes.
        """
        if line == "" or line is None:
            print(" ** class name missing ** ")
        else:
            arg = line.split(' ')
            if arg[0] not in storage.all_classes():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id is missing **")
            else:
                if f"{arg[0]}.{arg[1]}" not in storage.all():
                    print("** no instance found **")
                else:
                    del(storage.all()[f"{arg[0]}.{arg[1]}"])
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representations of instances.
        """
        if not line:
            list_str = [str(v) for k, v in storage.all().items()]
            print(list_str)
        elif line and line in storage.all_classes():
            list_str = [str(v) for k, v in storage.all().items()]
            print(list_str)
        else:
            if line not in storage.all_classes():
                print("** class doesn't exist **")

    def do_count(self, line):
        """
        Counts the number of instances of a class.
        """
        if line == "" or line is None:
            return

    def do_update(self, line):
        """
        Updates an attribute of an instance.
        """
        if line == "" or line is None:
            print(" ** class name missing ** ")
        else:
            arg = line.split(' ')
            if arg[0] not in storage.all_classes():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id is missing **")
            elif f"{arg[0]}.{arg[1]}" not in storage.all():
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                cls_name = arg[0]
                inst_id = arg[1]
                attr_name = arg[2]
                attr_value = arg[3]

                class_attributes = self._attrs.get(cls_name, {})
                # for k, v in class_attributes.items():
                #     print(f"{k} : {v}")
                if attr_name in class_attributes:
                    attr_type = class_attributes.get(attr_name)
                    # print(attr_type)
                    try:
                        attr_type(attr_value)
                    except (ValueError, TypeError) as e:
                        print(e)
                    else:
                        inst = storage.all()[f"{cls_name}.{inst_id}"]
                        setattr(inst, attr_name, attr_value)
                        storage.save()
                else:
                    print("invalid attribute name!")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

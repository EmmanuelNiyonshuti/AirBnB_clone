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

    def help_quit(self):
        print('Quit command to exit the program' + '\n')

    def do_EOF(self, line):
        """EOF to Exit the program"""
        return True

    def help_EOF(self):
        print("EOF to Exit the program")

    def emptyline(self):
        """
        pass when nothing is passed.
        """
        pass

    def do_create(self, line):
        if line is None or line == "":
            print("** class name missing **")
        elif line not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.all_classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        print("Creates a new instance and prints the id")

    def do_show(self, line):
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

    def help_show(self):
        print("Prints the string representation of an instance")

    def do_destroy(self, line):
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

    def help_destroy(self):
        print("Deletes an instance based on the class name and id")

    def do_all(self, line):
        if not line:
            list_str = [str(v) for k, v in storage.all().items()]
            print(list_str)
        elif line and line in storage.all_classes():
            list_str = [str(v) for k, v in storage.all().items()]
            print(list_str)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all string representation of all instances based"
              "or not on the class name")
        print("Ex: $ all BaseModel or $ all")

    def do_count(self, line):
        if line == "" or line is None:
            return

        class_name = line.split()[0]
        count = len(storage.all()[class_name])
        print(count)   

    def do_update(self, line):
        """
        Command: update <class_name> <instance_id> <attr_name> <attr_value>
        Updates the specified attr of the instance identified by <instance_id>
        belonging to the class <class_name> with the provided <attr_value>.
        Example: update User c331cb80-f2fc-4b68-8fd9-f12c10ef1a9f name "john"
        This updates the 'name' attribute of the BaseModel instance with ID
        'a032a0e2-199e-4692-8d3c-b19f65ae71c2' to 'New Name'
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
            try:
                class_attributes = self._attrs.get(cls_name, {})
                # print(class_attributes)
                if attr_name in class_attributes:
                    try:
                        attr_value = class_attributes[attr_name](attr_value)
                    except ValueError:
                        pass
            except UnboundLocalError:
                pass
            else:
                instance = storage.all()[f"{cls_name}.{inst_id}"]
                setattr(instance, attr_name, attr_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

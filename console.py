#!/usr/bin/python3
"""
This module comprises the entry point of the My console.
"""
import cmd
import re
import sys
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage



class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self,line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print('Quit command to exit the program'+ '\n')

    def do_EOF(self, line):
        """EOF to Exit the program"""
        return True

    def help_EOF(self):
        print("EOF to Exit the program")

    def emptyline(self):
        pass

    def do_create(self, line):
        if line == None or line == "":
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
        if line == None or line == "":
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
           print("** class does not exist **")
   
    def help_all(self):
        print("Prints all string representation of all instances based or not on the class name\nEx: $ all BaseModel or $ all")
    
    def do_count(self, line):
        pass
    """def do_update(self, line):
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.all_classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attr = storage.obj_attr()[classname]
                if attribute in attr:
                    value = attr[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
    def help_update(self):
        print("Updates an instance by adding or updating attribute.")"""



if __name__ == '__main__':
    HBNBCommand().cmdloop()
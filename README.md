                0x00. AirBnB clone - The console
![alt text](image.png)

Welcome to My AirBnB Clone project! This project is an essential step towards building a full web application. The primary goal of this initial phase is developing the backend and integrating it with a console application using the cmd module in Python.

Project Description
Data, represented as Python objects, is generated and stored in a JSON file, acting as a database. We built a storage system for storing our objects in a JSON file and retrieving them using the json module in Python 3.

The command-line interface mimics the Bash shell but with a limited set of commands tailored specifically for the AirBnB website's usage.

This command-line interpreter acts as the frontend of the web app, allowing users to interact with the backend developed using Python's object-oriented programming (OOP) paradigm.

Some of the available commands include:

show
create
update
destroy
count
Additionally, the following actions can be performed as part of the command-line interpreter's implementation, coupled with the backend and file storage system:

Creating new objects (e.g., a new User or a new Place)
Retrieving an object from a file, a database, etc.
Performing operations on objects (count, compute stats, etc.)
Updating attributes of an object
Destroying an object
Getting Started
These instructions will help you set up a copy of the project on your local machine (Linux distro) for development and testing purposes.

Installation
Clone the repository from GitHub. This will include the simple shell program and all its dependencies.

git clone https://github.com/jzamora5/AirBnB_clone.git
After cloning the repository, you'll find a folder named AirBnB_clone, containing several files necessary for the program to function:

console.py: The main executable of the project, the command interpreter.
models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON files to instances.
models/__init__.py: A unique FileStorage instance for the application.
models/base_model.py: Class that defines all common attributes/methods for other classes.
models/user.py: User class that inherits from BaseModel.
models/state.py: State class that inherits from BaseModel.
models/city.py: City class that inherits from BaseModel.
models/amenity.py: Amenity class that inherits from BaseModel.
models/place.py: Place class that inherits from BaseModel.
models/review.py: Review class that inherits from BaseModel.
Usage
The program can operate in two modes: interactive and non-interactive.

Interactive Mode
In interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After executing a command, the prompt will reappear, awaiting a new command. This loop continues until the user exits the program.

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-Interactive Mode
In non-interactive mode, the shell is run with a command input piped into its execution. The command is executed as soon as the shell starts, without displaying a prompt or expecting further input from the user.

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
Command Input Format
To issue commands to the console, they must be piped through an echo in the case of non-interactive mode.

In interactive mode, commands are entered via the keyboard when the prompt appears and are recognized upon pressing the Enter key (newline). The console will attempt to execute the command or display an error message if the command fails. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the quit command.

Arguments
Most commands accept several options or arguments when executing the program. To ensure the shell recognizes these parameters, separate them with spaces.

Example:

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py
or

user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py

AUTHOR:
NIYONSHUTI Emmanuel <nemmy0257@gmail.com>

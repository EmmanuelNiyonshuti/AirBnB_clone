# 0x00. AirBnB clone - The console
![image](https://github.com/EmmanuelNiyonshuti/AirBnB_clone/assets/142030687/9985dc8f-5826-4763-82f2-0d8688a44cb6)

## Project Description

Welcome to my AirBnB Clone project! This project is an essential step towards building a full web application. The primary goal of this initial phase is developing the backend and integrating it with a console application using the cmd module in Python.

### Data Storage

Data, represented as Python objects, is generated and stored in a JSON file, acting as a database. I built a storage system for storing my objects in a JSON file and retrieving them using the json module in Python 3.

### Command-Line Interface

The command-line interface mimics the Bash shell but with a limited set of commands tailored specifically for the AirBnB website's usage.

This command-line interpreter acts as the frontend of the web app, allowing users to interact with the backend developed using Python's object-oriented programming (OOP) paradigm.

for now some of the available commands includes:

- show
- create
- update
- count

Additionally, the following actions can be performed as part of the command-line interpreter's implementation, coupled with the backend and file storage system:

- Creating new objects (e.g., a new User or a new Place)
- Retrieving an object from a file, a database, etc.
- Destroying an object
- Counting the number of objects. 
## Getting Started

These instructions will help you set up a copy of the project on your local machine (Linux distro) for development and testing purposes.

### Installation

Clone the repository from GitHub. This will include the simple shell program and all its dependencies.

git clone https://github.com/jzamora5/AirBnB_clone.git

After cloning the repository, you'll find a folder named AirBnB_clone, containing several files necessary for the program to function:

console.py: The main executable of the project, the command interpreter.
models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON files to instances.
models/init.py: A unique FileStorage instance for the application.
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

Non-Interactive Mode

In non-interactive mode, the shell is run with a command input piped into its execution. The command is executed as soon as the shell starts, without displaying a prompt or expecting further input from the user.

$ echo "help" | ./console.py

Command Input Format

To issue commands to the console, they can be piped through an echo in the case of non-interactive mode.

In interactive mode, commands are entered via the keyboard when the prompt appears and are recognized upon pressing the Enter key (newline). The console will attempt to execute the command or display an error message if the command fails. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the quit command.

Arguments

Most commands accept several options or arguments when executing the program. To ensure the shell recognizes these parameters, separate them with spaces.

Example:

$ ./console.py
(hbnb) create BaseModel

or

$ ./console.py
$ echo "create BaseModel" | ./console.py

Author
NIYONSHUTI Emmanuel

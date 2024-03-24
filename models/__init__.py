#!/usr/bin/python3
"""
This module comprises the creation of the unique file storage instance
which will serve in adding new instances and saving them to a json file.
it will also serve in integrating file storage with the console.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
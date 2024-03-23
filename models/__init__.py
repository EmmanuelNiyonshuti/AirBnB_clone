"""
This module comprises the creation of the instance
of file storage which will serve in adding new instances
and saving them to a json file.
it will also serve in integrating file storage with the console.
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

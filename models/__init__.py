#!/usr/bin/python3
"""
This module comprises the initialization of the package.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

#!/usr/bin/python3
"""
This module comprises a subclass of base module class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
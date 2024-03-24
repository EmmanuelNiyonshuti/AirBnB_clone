#!/usr/bin/python3
"""
This module comprises a subclass of base module class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
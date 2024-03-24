#!/usr/bin/python3
"""
This module comprises a subclass of base model class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """State Class"""
    State_id = ""
    name = ""

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        return {
                '__class__': __class__.__name__,
                **self.__dict__,
                'created_at': self.created_at.isoformat('T'),
                'updated_at': self.updated_at.isoformat('T')
                 }

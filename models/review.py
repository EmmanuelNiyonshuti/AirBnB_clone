#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        return {
                '__class__': __class__.__name__,
                **self.__dict__,
                'created_at': self.created_at.isoformat('T'),
                'updated_at': self.updated_at.isoformat('T')
                 }

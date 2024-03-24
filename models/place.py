#!/usr/bin/python3
"""
This module comprises a subclass of base module class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        return {
                '__class__': __class__.__name__,
                **self.__dict__,
                'created_at': self.created_at.isoformat('T'),
                'updated_at': self.updated_at.isoformat('T')
                 }
    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"


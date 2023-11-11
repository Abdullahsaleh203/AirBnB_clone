#!/usr/bin/python3
"""This module creates the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects
    Represent an amenity.
    Attributes:
    name (str): The name of the amenity.
    """
    name = ""

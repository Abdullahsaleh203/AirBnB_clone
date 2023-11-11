#!/usr/bin/python3
"""This module creates a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects
    Represent a city.
    Attributes:
        state_id (str): the state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""

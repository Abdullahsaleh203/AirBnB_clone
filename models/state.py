#!/usr/bin/python3
""" Module to get the BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):

    """Class for managing state objects
    Represent a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""

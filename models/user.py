#!/usr/bin/python3
""" Module to get the BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects
    Represent a User.
    Attributes:
        email (str): the email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

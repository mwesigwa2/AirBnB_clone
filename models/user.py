#!/usr/bin/python3
<<<<<<< HEAD
"""
Definititon of user class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User: Definition of  data describing users, it inherits from BaseModel class

    Variables:
        email (string): Email of user stored as a string.
        password (string): User password.
        first_name (string): Users first name.
        last_name (string): Users last name.
    """
=======
# module that defines the class User
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
>>>>>>> 6a2a1a848a83016ff60690bab2a9ffa6868299aa
    email = ""
    password = ""
    first_name = ""
    last_name = ""

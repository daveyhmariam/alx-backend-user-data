#!/usr/bin/env python3
"""Module for Authentication
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Returns hashed password string

    Args:
        password (str):

    Returns:
        str:
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Checks if a user with the given email
            already exists, hashes the password if necessary, and adds a
            new user to the database.

        Args:
            email (str):
            password (str):

        Raises:
            ValueError:

        Returns:
            User:
        """
        user = None
        try:
            user = self._db.find_user_by(**{'email': email})
        except (InvalidRequestError, NoResultFound):
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

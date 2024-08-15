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


def _generate_uuid() -> str:
    """
    returns a randomly generated UUID.
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if the provided email and
            password match a user's credentials in the database.

        Args:
            email (str):
            password (str):

        Returns:
            bool:
        """
        user = None
        try:
            user = self._db.find_user_by(**{'email': email})
        except (InvalidRequestError, NoResultFound):
            return False
        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """
        updates the user's session ID in the database.

        Args:
            email (str):

        Returns:
            str:
        """
        try:
            user = self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return
        session_id = _generate_uuid()
        self._db.update_user(user.id, **{'session_id': session_id})
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """retrieves a user from
            the database based on a given session ID.

        Args:
            session_id (str):

        Returns:
            User:
        """
        try:
            user = self._db.find_user_by(**{'session_id': session_id})
        except (InvalidRequestError, NoResultFound):
            return
        return user

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user's session ID to None


        Args:
            user_id (int):

        Returns:
            _type_:
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None

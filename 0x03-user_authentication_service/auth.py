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

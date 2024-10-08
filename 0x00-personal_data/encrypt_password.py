#!/usr/bin/env python3
"""encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashing.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checking if a hashed password

    Args:
        hashed_password
        password (str):

    Returns:
        bool:
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

#!/usr/bin/env python3
"""encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashing.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

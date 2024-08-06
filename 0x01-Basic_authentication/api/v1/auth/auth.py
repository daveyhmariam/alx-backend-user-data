#!/usr/bin/env python3
"""
Auth class definition
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            path (str):
            excluded_paths (List[str]):

        Returns:
            bool:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """

        Args:
            request (_type_, optional): Defaults to None.

        Returns:
            str:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """

        Returns:
            User:
        """
        return None

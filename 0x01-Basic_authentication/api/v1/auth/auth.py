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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or (path + "/") in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """

        Args:
            request (_type_, optional): Defaults to None.

        Returns:
            str:
        """
        if request is None or "Authorization" not in request.headers.keys():
            return None
        else:
            return (request.headers["Authorization"])

    def current_user(self, request=None) -> TypeVar('User'):
        """

        Returns:
            User:
        """
        return None

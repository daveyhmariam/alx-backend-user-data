#!/usr/bin/env python3
"""
Authenticating with basic auth class definition
"""

from api.v1.auth.auth import Auth
import re
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """class definition of basic auth

       Auth (class): base class for authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Decode authorization header

        Args:
            authorization_header (str): request header under Authorization

        Returns:
            str: credential string
        """
        if (authorization_header is None
            or
                not isinstance(authorization_header, str)):
            return None

        match = re.match(r'^Basic\s', authorization_header)
        if match is not None:
            return authorization_header.strip(match.group())

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string

        Args:
            base64_authorization_header (str): encoded base64 string
        Returns:
            str: decoded string in utf-8 format
        """
        if (base64_authorization_header is None or
            not isinstance(base64_authorization_header,
                           str)):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None
        pat = r'(?P<user>[^:]+):(?P<password>.+)'
        match = re.fullmatch(pat, decoded_base64_authorization_header.strip())
        if match is not None:
            return match.group('user'), match.group('password')
        return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password.
        """
        if ((not user_email or not isinstance(user_email, str)) and
                (not user_pwd or not isinstance(user_pwd, str))):
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
            if user[0].is_valid_password(user_pwd):
                return user
        return None

#!/usr/bin/env python3
"""
Authenticating with basic auth class definition
"""

from api.v1.auth.auth import Auth
import re
import base64
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string

        Args:
            base64_authorization_header (str): encoded base64 string
        Returns:
            str: decoded string in utf-8 format 
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

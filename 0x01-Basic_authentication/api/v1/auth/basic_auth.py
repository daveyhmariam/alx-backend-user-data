#!/usr/bin/env python3
"""
Authenticating with basic auth class definition
"""

from api.v1.auth.auth import Auth
import re


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

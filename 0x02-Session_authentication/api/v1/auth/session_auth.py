#!/usr/bin/env python3
"""
class definition of new authentication mechanism:
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """session authentication

    Args:
        Auth (Base class)
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """create session id (uuid4) for user id

        Args:
            user_id (str, optional): id of the user object

        Returns:
            str: session id
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

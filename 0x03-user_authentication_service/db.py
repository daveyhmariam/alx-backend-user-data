#!/usr/bin/env python3
""" Database for ORM """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class definition
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database with the
            provided email and hashed password.

        Args:
            email (str):
            hashed_password (str):

        Returns:
            User:
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Searches for a user in the
            database based on the provided keyword arguments.

        Raises:
            InvalidRequestError:
            InvalidRequestError:
            NoResultFound:

        Returns:
            User:
        """
        if not kwargs:
            raise InvalidRequestError
        key = kwargs.keys()
        for k in key:
            if k not in User.__table__.columns:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user's information in a database based

        Args:
            user_id (int):

        Raises:
            ValueError:
            ValueError:
        """
        user = self.find_user_by(id=user_id)
        if not user:
            raise ValueError
        c = User.__table__.columns.keys()
        for k in kwargs.keys():
            if k not in c:
                raise ValueError
        for k, v in kwargs.items():
            setattr(user, k, v)
        self._session.commit()

#!/usr/bin/env python3
"""Class User for ORM class definition
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME, INTEGER


Base = declarative_base()


class User(Base):
    '''
    user ORM class
    '''
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

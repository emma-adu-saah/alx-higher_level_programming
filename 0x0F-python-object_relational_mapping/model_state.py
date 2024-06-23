#!/usr/bin/python3
"""Contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()


class State(Base):
    """Defines the Columns and attributes of the state table"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)

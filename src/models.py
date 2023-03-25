import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(400), nullable=False)
    password = Column(String(300), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    orbit = Column(String(250))
    population = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table vehicle.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table favorites.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}







# Definición de la clase Character
class Character(Base):
    __tablename__ = 'characters'
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    height = Column(Float(), nullable=False)
    mass = Column(Float(), nullable=False)
    hair_color=Column(String(50), nullable=False)
    skin_color=Column(String(50), nullable=False)
    eyes_color=Column(String(50), nullable=False)
    birth_year = Column(Float(), nullable=False)
    gender=Column(String(50), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    diameter = Column(Float(), nullable=False)
    rotation_period = Column(Float(), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Float(), nullable=False)
    Population = Column(Float(), nullable=False)
    climate = Column(String, nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    model = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    Manufacturer = Column(String, nullable=False)
    cost_in_credits = Column(Float(), nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Float(), nullable=False)

# Tabla User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    subscription_date = Column(String, nullable=False)
    birth_date = Column(Integer)
    country = Column(String)

# Tabla User_Character
class Favorite_Character(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_uid = Column(Integer, ForeignKey('characters.uid'), nullable=False)

# Tabla User_Planet
class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_uid = Column(Integer, ForeignKey('planets.uid'), nullable=False)

# Tabla User_Starship
class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    starship_uid = Column(Integer, ForeignKey('vehicles.uid'), nullable=False)


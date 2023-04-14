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
    users_favorited = relationship("Favorite_Character", back_populates="character")

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
    users_favorited = relationship("Favorite_Planet", back_populates="planet")

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
    users_favorited = relationship("Favorite_Vehicles", back_populates="vehicle")

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
    favorite_characters = relationship("Favorite_Character", back_populates="user")
    favorite_planets = relationship("Favorite_Planet", back_populates="user")
    favorite_vehicles = relationship("Favorite_Vehicles", back_populates="user")

class Favorite_Character(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_uid = Column(Integer, ForeignKey('characters.uid'), nullable=False)
    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character", back_populates="users_favorited")

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_uid = Column(Integer, ForeignKey('planets.uid'), nullable=False)
    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="users_favorited")

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    vehicle_uid = Column(Integer, ForeignKey('vehicles.uid'), nullable=False)
    user = relationship("User", back_populates="favorite_vehicles")
    vehicle = relationship("Vehicles", back_populates="users_favorited")








# # Definición de la clase Character
# class Character(Base):
#     __tablename__ = 'characters'
#     uid = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     url = Column(String(50), nullable=False)
#     height = Column(Float(), nullable=False)
#     mass = Column(Float(), nullable=False)
#     hair_color=Column(String(50), nullable=False)
#     skin_color=Column(String(50), nullable=False)
#     eyes_color=Column(String(50), nullable=False)
#     birth_year = Column(Float(), nullable=False)
#     gender=Column(String(50), nullable=False)
#     users_favorited = relationship("Favorite_Character", back_populates="character")


# class Planet(Base):
#     __tablename__ = 'planets'
#     uid = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     url = Column(String, nullable=False)
#     diameter = Column(Float(), nullable=False)
#     rotation_period = Column(Float(), nullable=False)
#     orbital_period = Column(Integer, nullable=False)
#     gravity = Column(Float(), nullable=False)
#     Population = Column(Float(), nullable=False)
#     climate = Column(String, nullable=False)
#     users_favorited = relationship("Favorite_Planet", back_populates="planet")


# class Vehicles(Base):
#     __tablename__ = 'vehicles'
#     uid = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     url = Column(String, nullable=False)
#     model = Column(String, nullable=False)
#     vehicle_class = Column(String, nullable=False)
#     Manufacturer = Column(String, nullable=False)
#     cost_in_credits = Column(Float(), nullable=False)
#     passengers = Column(Integer, nullable=False)
#     cargo_capacity = Column(Float(), nullable=False)
#     users_favorited = relationship("Favorite_Vehicles", back_populates="vehicle")


# # Tabla User
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     subscription_date = Column(String, nullable=False)
#     birth_date = Column(Integer)
#     country = Column(String)
#     favorite_characters = relationship("Favorite_Character", back_populates="user")
#     favorite_planets = relationship("Favorite_Planet", back_populates="user")
#     favorite_vehicles = relationship("Favorite_Vehicles", back_populates="user")



# # Tabla User_Character
# class Favorite_Character(Base):
#     __tablename__ = 'favorite_characters'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     character_uid = Column(Integer, ForeignKey('characters.uid'), nullable=False)
#     user = relationship("User", back_populates="favorite_characters")
#     character = relationship("Character", back_populates="users_favorited")

# # Tabla User_Planet
# class Favorite_Planet(Base):
#     __tablename__ = 'favorite_planet'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     planet_uid = Column(Integer, ForeignKey('planets.uid'), nullable=False)
#     user = relationship("User", back_populates="favorite_planets")
#     planet = relationship("Planet", back_populates="users_favorited")


# # Tabla User_Starship
# class Favorite_Vehicles(Base):
#     __tablename__ = 'favorite_vehicles'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     starship_uid = Column(Integer, ForeignKey('vehicles.uid'), nullable=False)
#     user = relationship("User", back_populates="favorite_vehicles")
#     vehicle = relationship("Vehicles", back_populates="users_favorited")
    

#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ Define data types of the table """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Return a new list with the object of cities """
            from models import storage
            from models.city import City
            cityList = []
            obj_city = storage.all(City)
            for key, value in obj_city.items():
                if value.state_id == self.id:
                    cityList.append(value)
            return cityList

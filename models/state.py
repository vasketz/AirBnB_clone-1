#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ Define data types of the table """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Return a new list with the object of cities """
            from models import storage
            cityList = []
            obj_city = storage.all(City)
            for items in obj_city.value():
                if items.state_id == self.id:
                    cityList.append(items)
            return cityList

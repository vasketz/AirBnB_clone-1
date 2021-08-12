#!/usr/bin/python3
""" Module DBStorage """

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PASSWORD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      USER, PASSWORD, HOST, DB),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Specify the classes to query """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            valueQuery = self.__session.query(cls)
        else:
            valueQuery = self.__session.query(State).all()
            valueQuery.extend(self.__session.query(City).all())
            valueQuery.extend(self.__session.query(User).all())
            valueQuery.extend(self.__session.query(Place).all())
            valueQuery.extend(self.__session.query(Review).all())
            valueQuery.extend(self.__session.query(Amenity).all())

        return {"{}.{}".format(type(obj).__name__, obj.id):
                obj for obj in valueQuery}

    def new(self, obj):
        """ Add a object to database """
        self.__session.add(obj)

    def save(self):
        """ Save a oject to database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete a object to database """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables to database """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.close()

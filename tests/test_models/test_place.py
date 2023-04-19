#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


    

class test_Place(test_basemodel):
    """ place tests class"""

    def __init__(self, *args, **kwargs):
        """ init test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ testing place city_id attr"""
        neww = self.value()
        self.assertEqual(type(neww.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ testing place user_id attr"""
        neww = self.value()
        self.assertEqual(type(neww.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ testing place name attr"""
        neww = self.value()
        self.assertEqual(type(neww.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """testing place description attr"""
        neww = self.value()
        self.assertEqual(type(neww.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """ testing place number of rooms attr"""
        neww = self.value()
        self.assertEqual(type(neww.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """ testing place number of bathrooms attr"""
        neww = self.value()
        self.assertEqual(type(neww.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """ testing place max_guest attr"""
        neww = self.value()
        self.assertEqual(type(neww.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """ testing place price by night attr"""
        neww = self.value()
        self.assertEqual(type(neww.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """ testing place latitud attr"""
        neww = self.value()
        self.assertEqual(type(neww.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """ testing place longitude attr"""
        neww = self.value()
        self.assertEqual(type(neww.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """ testing amenity ids"""
        neww = self.value()
        self.assertEqual(type(neww.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))


#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """ review test class"""

    def __init__(self, *args, **kwargs):
        """ review class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ testing review place_id attr"""
        neww = self.value()
        self.assertEqual(type(neww.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ testing review text attr"""
        neww = self.value()
        self.assertEqual(type(neww.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
    
    def test_user_id(self):
        """ testing review user_id attr"""
        neww = self.value()
        self.assertEqual(type(neww.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    
                         type(None))


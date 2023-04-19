#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os


class test_User(test_basemodel):
    """ test class for user model"""

    def __init__(self, *args, **kwargs):
        """ user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        
    def test_last_name(self):
        """ testing user last name attr"""
        neww = self.value()
        self.assertEqual(type(neww.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """ testing user email attr"""
        neww = self.value()
        self.assertEqual(type(neww.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """ testing user password attr"""
        neww = self.value()
        self.assertEqual(type(neww.password), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))


    def test_first_name(self):
        """ testing user first anme attr"""
        neww = self.value()
        self.assertEqual(type(neww.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    

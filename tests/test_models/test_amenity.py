#!/usr/bin/python3

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os


@classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass


class test_Amenity(test_basemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))


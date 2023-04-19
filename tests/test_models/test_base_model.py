#!/usr/bin/python3
""" """
from models.base_model import BaseModel, Base
from datetime import datetime
import unittest
from uuid import UUID
import json
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """ test class for base_model class"""

    def __init__(self, *args, **kwargs):
        """ init the test class of basemodel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ the set up method of the test class"""
        pass

    def tearDown(self):
        """the teardown method of the ctest class"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the model class.
        """
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """ default testing of basemodel"""
        e = self.value()
        self.assertEqual(type(e), self.value)

    def test_kwargs(self):
        """ testing basemodel with kwargs"""
        e = self.value()
        copy = e.to_dict()
        neww = BaseModel(**copy)
        self.assertFalse(neww is e)

    def test_kwargs_int(self):
        """ testing with kwargs again but with int kwargs"""
        e = self.value()
        copy = e.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            neww = BaseModel(**copy)

    def test_save(self):
        """ Testing save metthod"""
        e = self.value()
        e.save()
        key = self.name + "." + e.id
        with open('file.json', 'r') as f:
            k = json.load(f)
            self.assertEqual(k[key], e.to_dict())

    def test_str(self):
        """ testing the str method of themodel"""
        e = self.value()
        self.assertEqual(str(e), '[{}] ({}) {}'.format(self.name, e.id,
                         e.__dict__))

    def test_todict(self):
        """ testing the to_dict method"""
        e = self.value()
        n = e.to_dict()
        self.assertEqual(e.to_dict(), n)
        # Tests if it's a dictionary
        self.assertIsInstance(self.value().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())
        # Tests if to_dict contains added attributes
        mdl = self.value()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', self.value(firstname='Celestine').to_dict())
        self.assertIn('lastname', self.value(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = self.value()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': mdl.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.value(id='u-b34', age=13).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': 13
                }
            )
            self.assertDictEqual(
                self.value(id='u-b34', age=None).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': 'u-b34',
                    'age': None
                }
            )
        # Tests to_dict output contradiction
        mdl_d = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(45)
        self.assertNotIn('_sa_instance_state', n)

    def test_kwargs_none(self):
        """ testing kwargs again with none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            neww = self.value(**n)

    def test_kwargs_one(self):
        """ testing kwargs with one arg"""
        n = {'name': 'test'}
        neww = self.value(**n)
        self.assertEqual(neww.name, n['name'])

    def test_id(self):
        """ testing id attr of the model"""
        neww = self.value()
        self.assertEqual(type(neww.id), str)

    def test_created_at(self):
        """ testing created at attr"""
        neww = self.value()
        self.assertEqual(type(neww.created_at), datetime)

    def test_updated_at(self):
        """ testing updated at attr"""
        neww = self.value()
        self.assertEqual(type(neww.updated_at), datetime)
        n = neww.to_dict()
        neww = BaseModel(**n)
        self.assertFalse(neww.created_at == neww.updated_at)


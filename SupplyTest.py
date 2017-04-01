import unittest
from supply.database import *


class TestDatabase(unittest.TestCase):
    def set_product(self):
        db = Database().open()
        db.close()


class TestModel(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True, '')


class TestView(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True, '')


class TestController(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True, '')

if __name__ == '__main__':
    unittest.main()
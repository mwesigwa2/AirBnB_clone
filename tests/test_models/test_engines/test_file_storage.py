#!/usr/bin/python3
# test module for class FileStorage
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """sets up an instance of FileStorage for the test"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """cleans up after a test"""
        self.storage._FileStorage__objects = {}
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    """def test_reload_file_not_there(self):
        #tests the reload method in case file doesnt exits
        self.storage.reload()
        #since reload saves to __objects
        #a non existent file leads to an empty __objects
        self.assertEqual(len(self.storage.all()), 0)"""

        def test_save_and_reload(self):
        """test the save and reload methods"""
        
        # Save instances to file
        self.storage.save()

        # Reload instances from file
        self.storage.reload()

        def test_save_file_exists(self):
            """test if file from save method is exists"""
        # save to file
        self.storage.save()

        # check if file exists
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()

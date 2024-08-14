# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:04:10 2024

@author: Administrator
This script contains a unit test for the SaasWorkOrderStructure class,
 verifying that the generate_documentation method correctly generates
 both text and JSON documentation files with the expected content structure.
"""

import unittest
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
parent_directory3 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataStructured/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
sys.path.insert(0, parent_directory3)
import json
from saas_work_order_structure import SaasWorkOrderStructure

class TestSaasWorkOrderStructure(unittest.TestCase):

    def setUp(self):
        self.structure = SaasWorkOrderStructure()
        self.txt_filename = "SaasWorkOrderStructure_Documentation.txt"
        self.json_filename = "SaasWorkOrderStructure_Documentation.json"

    def tearDown(self):
        # Clean up the generated files after the test
        if os.path.exists(self.txt_filename):
            os.remove(self.txt_filename)
        if os.path.exists(self.json_filename):
            os.remove(self.json_filename)

    def test_generate_documentation(self):
        # Generate the documentation
        self.structure.generate_documentation()

        # Check if the text file is created
        self.assertTrue(os.path.exists(self.txt_filename), "Text documentation file was not created.")

        # Check if the JSON file is created
        self.assertTrue(os.path.exists(self.json_filename), "JSON documentation file was not created.")

        # Verify the content of the JSON file
        with open(self.json_filename, 'r') as json_file:
            data = json.load(json_file)
            self.assertIsInstance(data, list, "JSON file content is not a list.")
            self.assertTrue(len(data) > 0, "JSON file content is empty.")
            self.assertIn("name", data[0], "JSON file content does not contain expected keys.")
            self.assertIn("type", data[0], "JSON file content does not contain expected keys.")
            self.assertIn("description", data[0], "JSON file content does not contain expected keys.")
            self.assertIn("rules", data[0], "JSON file content does not contain expected keys.")

if __name__ == "__main__":
    unittest.main()

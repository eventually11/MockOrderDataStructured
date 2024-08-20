# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:05:48 2024

@author: Administrator
This script provides unit tests for the SaasTaskDataStructure class,
 verifying the generation and content of the documentation files in both text 
 and JSON formats. The tests ensure that the files are correctly 
 created and contain expected data.
"""


import os
import sys


from MockOrderDataStructured.saas_task_data_structure import SaasTaskDataStructure
import unittest
import json

class TestSaasTaskDataStructure(unittest.TestCase):

    def setUp(self):
        self.structure = SaasTaskDataStructure()
        self.structure.generate_documentation()

    def test_txt_documentation_generated(self):
        """Test that the text documentation file is generated and contains content."""
        txt_file_path = "SaasTaskDataStructure_Documentation.txt"
        self.assertTrue(os.path.exists(txt_file_path), "Text documentation file was not generated.")
        
        with open(txt_file_path, "r") as file:
            content = file.read()
            self.assertIn("Field Name: task_id", content, "Text documentation file does not contain expected content.")

    def test_json_documentation_generated(self):
        """Test that the JSON documentation file is generated and contains valid JSON."""
        json_file_path = "SaasTaskDataStructure_Documentation.json"
        self.assertTrue(os.path.exists(json_file_path), "JSON documentation file was not generated.")
        
        with open(json_file_path, "r") as file:
            try:
                data = json.load(file)
                self.assertIsInstance(data, list, "JSON documentation does not contain a list.")
                self.assertIn("task_id", data[0]["name"], "JSON documentation does not contain expected field.")
            except json.JSONDecodeError:
                self.fail("JSON documentation file contains invalid JSON.")

    def tearDown(self):
        """Clean up generated files after tests."""
        os.remove("SaasTaskDataStructure_Documentation.txt")
        os.remove("SaasTaskDataStructure_Documentation.json")

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:10:34 2024

@author: Administrator

This unit test verifies that the generate_documentation method in the 
SaasPartnerOrderDataStructure class correctly creates both a text and a 
JSON file documenting the data structure. It ensures that the 
files are generated and then cleans up by deleting them after the test.
"""
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)

import unittest
from saas_partner_order_structure import SaasPartnerOrderDataStructure  # Adjust the import path as needed

class TestSaasPartnerOrderDataStructure(unittest.TestCase):

    def test_generate_documentation(self):
        # Create an instance of the SaasPartnerOrderDataStructure class
        structure = SaasPartnerOrderDataStructure()

        # Call the generate_documentation method
        structure.generate_documentation()

        # Check if the text file was created
        self.assertTrue(os.path.isfile("SaasPartnerOrderDataStructure_Documentation.txt"), "Text documentation file was not created.")
        
        # Check if the JSON file was created
        self.assertTrue(os.path.isfile("SaasPartnerOrderDataStructure_Documentation.json"), "JSON documentation file was not created.")

        # Clean up after the test (remove the generated files)
        os.remove("SaasPartnerOrderDataStructure_Documentation.txt")
        os.remove("SaasPartnerOrderDataStructure_Documentation.json")

if __name__ == "__main__":
    unittest.main()

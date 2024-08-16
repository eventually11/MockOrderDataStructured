# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:25:55 2024

@author: Administrator
This script defines a SaasPartnerOrderDataStructure class, 
which generates and documents the data structure for SaaS partner orders.
 It includes methods for generating random order data based on specified
 rules and outputs documentation in both text and JSON formats.
 The documentation covers field names, data types, descriptions, 
 and generation rules.
"""

import pandas as pd
from faker import Faker
import random
from hypothesis.strategies import integers, text, floats, composite, datetimes, timedeltas
from datetime import datetime, timedelta
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
from route_info_saver import RouteInfoToMySQL
import json


class SaasPartnerOrderDataStructure:
    """
    A class that defines the data structure for SaaS partner orders.
    """

    def __init__(self):
        self.fake = Faker()
        self.order_id_list = list(range(1000000, 10000000))
        random.shuffle(self.order_id_list)  # Shuffle to randomize order
        # Load the address pool from the CSV file
        csv_file_path = os.path.join(parent_directory, 'route_info_output.csv')
        df = pd.read_csv(csv_file_path)
        self.address_pool = df['address'].dropna().unique().tolist()

    @composite
    def generate_order_data(draw, self, address_pool):
        """
        Strategy to generate SaaS partner order data.

        Parameters
        ----------
        address_pool : list
            A list of addresses to choose from.

        Returns
        -------
        dict
            A dictionary containing the generated order data.
        """
        service_fee = round(draw(floats(min_value=0.01, max_value=10000.0)), 2)
        
        min_datetime = datetime(2020, 1, 1)
        max_datetime = datetime(2024, 12, 31)

        start_time = draw(datetimes(min_value=min_datetime, max_value=max_datetime))
        min_duration = timedelta(minutes=2)
        max_duration = timedelta(hours=1)
        end_time = start_time + draw(timedeltas(min_value=min_duration, max_value=max_duration))

        start_address = random.choice(address_pool)
        end_address = random.choice(address_pool)
        while end_address == start_address:
            end_address = random.choice(address_pool)

        return {
            'order_id': self.order_id_list.pop(),
            'tenant': draw(integers(min_value=1, max_value=1000)),
            'flow': draw(integers(min_value=1, max_value=100)),
            'sender': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'hub': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'dispatch_pool': draw(integers(min_value=1, max_value=100)),
            'vehicle_type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start_time': start_time,
            'end_time': end_time,
            'title': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'route_description': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'tags': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'overview': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'content': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start': start_address,
            'end': end_address,
            'service_fee': service_fee,
            'start_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'end_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'status_group': draw(integers(min_value=1, max_value=10))
        }


    def generate_documentation(self):
        fields = [
            {
                "name": "order_id",
                "type": "INT",
                "description": "Unique identifier for each order.",
                "rules": "Randomly generated integer between 1,000,000 and 10,000,000."
            },
            {
                "name": "tenant",
                "type": "INT",
                "description": "Identifier for the tenant who owns the order.",
                "rules": "Randomly generated integer between 1 and 1,000."
            },
            {
                "name": "flow",
                "type": "INT",
                "description": "Flow identifier related to the order process.",
                "rules": "Randomly generated integer between 1 and 100."
            },
            {
                "name": "sender",
                "type": "VARCHAR(255)",
                "description": "Name or ID of the sender.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "hub",
                "type": "VARCHAR(255)",
                "description": "Identifier for the hub processing the order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "dispatch_pool",
                "type": "INT",
                "description": "Identifier for the dispatch pool handling the order.",
                "rules": "Randomly generated integer between 1 and 100."
            },
            {
                "name": "vehicle_type",
                "type": "VARCHAR(50)",
                "description": "Type of vehicle used for the order (e.g., car, bike, van).",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "start_time",
                "type": "DATETIME",
                "description": "Timestamp when the order process starts.",
                "rules": "Randomly generated datetime between January 1, 2020, and December 31, 2024."
            },
            {
                "name": "end_time",
                "type": "DATETIME",
                "description": "Timestamp when the order process ends.",
                "rules": "Calculated as start_time plus a random duration between 2 minutes and 1 hour."
            },
            {
                "name": "title",
                "type": "VARCHAR(255)",
                "description": "Title or description of the order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "route_description",
                "type": "TEXT",
                "description": "Detailed description of the route taken for the order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "tags",
                "type": "VARCHAR(255)",
                "description": "Tags associated with the order for categorization.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "overview",
                "type": "TEXT",
                "description": "Overview or summary of the order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "content",
                "type": "TEXT",
                "description": "Detailed content or notes about the order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "type",
                "type": "VARCHAR(50)",
                "description": "Type of the order (e.g., delivery, pickup).",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "start",
                "type": "VARCHAR(255)",
                "description": "Start address or location for the order.",
                "rules": "Randomly selected address from the address_pool."
            },
            {
                "name": "end",
                "type": "VARCHAR(255)",
                "description": "End address or location for the order.",
                "rules": "Randomly selected address from the address_pool (different from start)."
            },
            {
                "name": "service_fee",
                "type": "DECIMAL(10, 2)",
                "description": "Fee associated with the order.",
                "rules": "Randomly generated decimal value between 0.01 and 10,000.00."
            },
            {
                "name": "start_task_validation",
                "type": "VARCHAR(255)",
                "description": "Validation information for the start task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "end_task_validation",
                "type": "VARCHAR(255)",
                "description": "Validation information for the end task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "status_group",
                "type": "INT",
                "description": "Status group identifier for tracking the order's status.",
                "rules": "Randomly generated integer between 1 and 10."
            }
        ]

        # Writing the documentation to a text file
        with open("SaasPartnerOrderDataStructure_Documentation.txt", "w") as file:
            for field in fields:
                file.write(f"Field Name: {field['name']}\n")
                file.write(f"Type: {field['type']}\n")
                file.write(f"Description: {field['description']}\n")
                file.write(f"Rules: {field['rules']}\n")
                file.write("\n")
        # Writing the documentation to a JSON file
        with open("SaasPartnerOrderDataStructure_Documentation.json", "w") as json_file:
            json.dump(fields, json_file, indent=4)
# Usage example
if __name__ == "__main__":
    structure = SaasPartnerOrderDataStructure()
    structure.generate_documentation()
    print("Documentation generated and saved to 'SaasPartnerOrderDataStructure_Documentation.txt'")
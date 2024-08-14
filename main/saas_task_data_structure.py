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
import json


class SaasTaskDataStructure:
    
    def __init__(self):
        self.fake = Faker()
        self.task_id_list = list(range(10000000, 100000000))
        self.order_id_list = list(range(1000000, 10000000))
        random.shuffle(self.order_id_list)  # Shuffle to randomize order
        csv_file_path = os.path.join(parent_directory, 'route_info_output.csv')
        df = pd.read_csv(csv_file_path)
        self.address_pool = df['address'].dropna().unique().tolist()

    @composite
    def saas_task_data(draw, self):
        service_fee = round(draw(floats(min_value=0.01, max_value=10000.0)), 2)
        
        min_datetime = datetime(2020, 1, 1)
        max_datetime = datetime(2024, 12, 31)

        start_time = draw(datetimes(min_value=min_datetime, max_value=max_datetime))
        min_duration = timedelta(minutes=2)
        max_duration = timedelta(hours=1)
        end_time = start_time + draw(timedeltas(min_value=min_duration, max_value=max_duration))

        start_address = random.choice(self.address_pool)
        end_address = random.choice(self.address_pool)
        while end_address == start_address:
            end_address = random.choice(self.address_pool)

        return {
            'task_id': self.task_id_list.pop(),
            'tenant': draw(integers(min_value=1, max_value=1000)),
            'order_id': random.choice(self.order_id_list),
            'sender': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'hub': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'zone': draw(integers(min_value=1, max_value=100)),
            'flow': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'task_pool': draw(integers(min_value=1, max_value=1000)),
            'partner': draw(integers(min_value=1, max_value=1000)),
            'title': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'content': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'date': start_time,
            'time_slot': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'service_time': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start': start_address,
            'end': end_address,
            'service_fee': service_fee,
            'items': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'end_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'status_code': draw(integers(min_value=1, max_value=10)),
            'status_group': draw(integers(min_value=1, max_value=10))
        }
    
    def generate_documentation(self):
        """
        Generates a documentation file with details about the data fields used in the SaasTaskDataStructure.
        The documentation is saved both as a text file and a JSON file.
        """

        fields = [
            {
                "name": "task_id",
                "type": "INT",
                "description": "Unique identifier for each task.",
                "rules": "Randomly generated integer between 10,000,000 and 100,000,000."
            },
            {
                "name": "tenant",
                "type": "INT",
                "description": "Identifier for the tenant who owns the task.",
                "rules": "Randomly generated integer between 1 and 1,000."
            },
            {
                "name": "order_id",
                "type": "INT",
                "description": "Identifier for the order associated with the task.",
                "rules": "Randomly selected from the available order IDs."
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
                "description": "Identifier for the hub processing the task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "zone",
                "type": "INT",
                "description": "Zone identifier for the task.",
                "rules": "Randomly generated integer between 1 and 100."
            },
            {
                "name": "flow",
                "type": "VARCHAR(255)",
                "description": "Flow identifier related to the task process.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "task_pool",
                "type": "INT",
                "description": "Identifier for the task pool handling the task.",
                "rules": "Randomly generated integer between 1 and 1,000."
            },
            {
                "name": "partner",
                "type": "INT",
                "description": "Partner identifier associated with the task.",
                "rules": "Randomly generated integer between 1 and 1,000."
            },
            {
                "name": "title",
                "type": "VARCHAR(255)",
                "description": "Title or description of the task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "content",
                "type": "TEXT",
                "description": "Detailed content or notes about the task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "date",
                "type": "DATETIME",
                "description": "Timestamp when the task is scheduled.",
                "rules": "Randomly generated datetime between January 1, 2020, and December 31, 2024."
            },
            {
                "name": "time_slot",
                "type": "VARCHAR(50)",
                "description": "Time slot allocated for the task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "type",
                "type": "VARCHAR(50)",
                "description": "Type of the task (e.g., delivery, pickup).",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "service_time",
                "type": "VARCHAR(50)",
                "description": "Time required to complete the task.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "start",
                "type": "VARCHAR(255)",
                "description": "Start address or location for the task.",
                "rules": "Randomly selected address from the address_pool."
            },
            {
                "name": "end",
                "type": "VARCHAR(255)",
                "description": "End address or location for the task.",
                "rules": "Randomly selected address from the address_pool (different from start)."
            },
            {
                "name": "service_fee",
                "type": "DECIMAL(10, 2)",
                "description": "Fee associated with the task.",
                "rules": "Randomly generated decimal value between 0.01 and 10,000.00."
            },
            {
                "name": "items",
                "type": "TEXT",
                "description": "Items involved in the task.",
                "rules": "Random string consisting of alphanumeric characters."
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
                "name": "status_code",
                "type": "INT",
                "description": "Status code for tracking the task's progress.",
                "rules": "Randomly generated integer between 1 and 10."
            },
            {
                "name": "status_group",
                "type": "INT",
                "description": "Status group identifier for the task.",
                "rules": "Randomly generated integer between 1 and 10."
            }
        ]

        # Writing the documentation to a text file
        with open("SaasTaskDataStructure_Documentation.txt", "w") as file:
            for field in fields:
                file.write(f"Field Name: {field['name']}\n")
                file.write(f"Type: {field['type']}\n")
                file.write(f"Description: {field['description']}\n")
                file.write(f"Rules: {field['rules']}\n")
                file.write("\n")
        
        # Writing the documentation to a JSON file
        with open("SaasTaskDataStructure_Documentation.json", "w") as json_file:
            json.dump(fields, json_file, indent=4)

# Usage example
if __name__ == "__main__":
    structure = SaasTaskDataStructure()
    structure.generate_documentation()
    print("Documentation generated and saved to 'SaasTaskDataStructure_Documentation.txt' ")
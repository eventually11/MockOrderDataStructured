# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:25:55 2024

@author: Administrator
This script defines a SaasWorkOrderStructure class that generates synthetic 
work order data for SaaS applications.
 It includes methods to create realistic work order entries with fields 
 like addresses, fees, and timestamps, using randomized data. Additionally, 
 the class can generate and save detailed documentation of the data 
 structure in both text and JSON formats.
"""

import pandas as pd
from faker import Faker
import random
from hypothesis.strategies import integers, text, floats, datetimes, timedeltas, composite, sampled_from
from datetime import datetime, timedelta
import os
import sys
import json


class SaasWorkOrderStructure:
    
    def __init__(self):
        self.fake = Faker()
        self.work_id_list = list(range(100000, 1000000))
        self.order_id_list = list(range(1000000, 10000000))
        random.shuffle(self.order_id_list)  # Shuffle to randomize order
        
        # Load the address and distance data from the CSV file into a dictionary
        try :
            csv_file_path = '../../../MockOrderDataImporter/output/route_info_output.csv'
            df = pd.read_csv(csv_file_path)
        except :
            print("first try")
            
        try :
            csv_file_path = '../../MockOrderDataImporter/output/route_info_output.csv'
            df = pd.read_csv(csv_file_path)
        except :
            print("second try")
            
        try :
            csv_file_path = '../MockOrderDataImporter/output/route_info_output.csv'
            df = pd.read_csv(csv_file_path)
        except :
            print("third try")
            self.address_pool = df['address'].dropna().unique().tolist()
    
    @composite
    def saas_work_order(draw, self, address_pool):
        service_fee = round(draw(floats(min_value=0.01, max_value=10000.0)), 2)
        
        min_datetime = datetime(2020, 1, 1)
        max_datetime = datetime(2024, 12, 31)

        start_time = draw(datetimes(min_value=min_datetime, max_value=max_datetime))
        min_duration = timedelta(minutes=2)
        max_duration = timedelta(hours=1)
        end_time = start_time + draw(timedeltas(min_value=min_duration, max_value=max_duration))

        start_address = draw(sampled_from(self.address_pool))
        end_address = draw(sampled_from([address for address in self.address_pool if address != start_address]))

        while end_address == start_address:
            end_address = random.choice(self.address_pool)
        
        # Retrieve the distance for the selected addresses
        # start_distance = self.address_distance_map[start_address]
        # end_distance = self.address_distance_map[end_address]

        return {
            'work_id': self.work_id_list.pop(),
            'tenant': draw(integers(min_value=1, max_value=1000)),
            'order_id': random.choice(self.order_id_list),
            'sender': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'flow': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'hub': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'zone': draw(integers(min_value=1, max_value=100)),
            'start_date': start_time,
            'start_time': start_time,
            'end_date': end_time,
            'end_time': end_time,
            'start': start_address,
            'end': end_address,
            'items': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'references': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'fee': service_fee,
            'reviewed': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'scheduled_time': start_time,
            'auto_publish_time': start_time,
            'status_code': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'estimation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'distance': draw(integers(min_value=1, max_value=1000)),  # Calculate distance based on start and end
            'channel': draw(integers(min_value=1, max_value=10))
        }
    
    
    
    def generate_documentation(self,output_directory):
        fields = [
            {
                "name": "work_id",
                "type": "INT",
                "description": "Unique identifier for each work order.",
                "rules": "Randomly generated integer between 100,000 and 1,000,000."
            },
            {
                "name": "tenant",
                "type": "INT",
                "description": "Identifier for the tenant.",
                "rules": "Randomly generated integer between 1 and 1,000."
            },
            {
                "name": "order_id",
                "type": "INT",
                "description": "Identifier for the associated order.",
                "rules": "Randomly selected from existing order IDs."
            },
            {
                "name": "sender",
                "type": "VARCHAR(255)",
                "description": "Name or ID of the sender.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "flow",
                "type": "VARCHAR(255)",
                "description": "Flow information related to the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "hub",
                "type": "VARCHAR(255)",
                "description": "Hub information associated with the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "zone",
                "type": "INT",
                "description": "Zone information for the work order.",
                "rules": "Randomly generated integer between 1 and 100."
            },
            {
                "name": "start_date",
                "type": "DATETIME",
                "description": "Start date and time of the work order.",
                "rules": "Randomly generated datetime between January 1, 2020, and December 31, 2024."
            },
            {
                "name": "start_time",
                "type": "DATETIME",
                "description": "Start time of the work order.",
                "rules": "Same as start_date."
            },
            {
                "name": "end_date",
                "type": "DATETIME",
                "description": "End date and time of the work order.",
                "rules": "Calculated as start_time plus a random duration between 2 minutes and 1 hour."
            },
            {
                "name": "end_time",
                "type": "DATETIME",
                "description": "End time of the work order.",
                "rules": "Same as end_date."
            },
            {
                "name": "start",
                "type": "VARCHAR(255)",
                "description": "Start address for the work order.",
                "rules": "Randomly selected address from the address pool."
            },
            {
                "name": "end",
                "type": "VARCHAR(255)",
                "description": "End address for the work order.",
                "rules": "Randomly selected address from the address pool (different from start)."
            },
            {
                "name": "items",
                "type": "TEXT",
                "description": "Items associated with the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "references",
                "type": "TEXT",
                "description": "References for the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "fee",
                "type": "DECIMAL(10, 2)",
                "description": "Fee associated with the work order.",
                "rules": "Randomly generated decimal value between 0.01 and 10,000.00."
            },
            {
                "name": "reviewed",
                "type": "VARCHAR(255)",
                "description": "Review status of the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "scheduled_time",
                "type": "DATETIME",
                "description": "Scheduled time for the work order.",
                "rules": "Same as start_time."
            },
            {
                "name": "auto_publish_time",
                "type": "DATETIME",
                "description": "Auto-publish time for the work order.",
                "rules": "Same as start_time."
            },
            {
                "name": "status_code",
                "type": "VARCHAR(255)",
                "description": "Status code of the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "estimation",
                "type": "VARCHAR(255)",
                "description": "Estimation details of the work order.",
                "rules": "Random string consisting of alphanumeric characters."
            },
            {
                "name": "distance",
                "type": "DECIMAL(10, 2)",
                "description": "Calculated distance between the start and end addresses.",
                "rules": "Absolute difference between distances of start and end addresses."
            },
            {
                "name": "channel",
                "type": "INT",
                "description": "Channel identifier for the work order.",
                "rules": "Randomly generated integer between 1 and 10."
            }
        ]

        # Writing the documentation to a text file
        with open("{0}/SaasWorkOrderStructure_Documentation.txt".format(output_directory), "w") as file:
            for field in fields:
                file.write(f"Field Name: {field['name']}\n")
                file.write(f"Type: {field['type']}\n")
                file.write(f"Description: {field['description']}\n")
                file.write(f"Rules: {field['rules']}\n")
                file.write("\n")

        # Writing the documentation to a JSON file
        with open("{0}SaasWorkOrderStructure_Documentation.json".format(output_directory), "w") as json_file:
            json.dump(fields, json_file, indent=4)

# Usage example
# if __name__ == "__main__":
#     structure = SaasWorkOrderStructure()
#     structure.generate_documentation()
#     print("Documentation generated and saved to 'SaasWorkOrderStructure_Documentation.txt'")
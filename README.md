# Partner Order Table Structure
This project is a Python-based tool designed to define the structure of tables for partner orders.
The defined structures can be used to ensure consistency in data storage, database schema design, 
and to serve as a foundation for generating synthetic data for testing, analysis, and validation purposes.


## Introduction
The Order Table Structure tool is intended for developers, data architects, and database administrators to define and maintain consistent table schemas for partner orders. This is crucial for ensuring that the data model is well-structured, normalized, and ready for integration with other systems


## Features
Generate random order data with various attributes like order_id, tenant, flow, sender, service_fee, etc.

## Output

When defining the table structure, the output example should be like this:

    order_id: INT - Unique identifier for each order.
    tenant: INT - Identifier for the tenant.
    flow: INT - Flow identifier related to the order process.
    sender: VARCHAR(255) - Name or ID of the sender.
    hub: VARCHAR(255) - Identifier for the hub processing the order.
    dispatch_pool: INT - Identifier for the dispatch pool.
    vehicle_type: VARCHAR(50) - Type of vehicle used for the order.
    start_time: DATETIME - Timestamp when the order process starts.
    end_time: DATETIME - Timestamp when the order process ends.
    title: VARCHAR(255) - Title or description of the order.
    route_description: TEXT - Detailed description of the route taken.
    tags: VARCHAR(255) - Tags associated with the order for categorization.
    overview: TEXT - Overview or summary of the order.
    content: TEXT - Detailed content or notes about the order.
    type: VARCHAR(50) - Type of the order (e.g., delivery, pickup).
    start: VARCHAR(255) - Start address or location.
    end: VARCHAR(255) - End address or location.
    service_fee: DECIMAL(10, 2) - Fee associated with the order.
    start_task_validation: VARCHAR(255) - Validation information for the start task.
    end_task_validation: VARCHAR(255) - Validation information for the end task.
    status_group: INT - Status group identifier for order tracking.
    
The primary output of each structure descriptor includes two key files:

Text File: A text file (txt) that documents the structure of the SaaS partner orders. It includes detailed information about each field, such as its name, type, description, and any rules or constraints applied.

JSON File: A JSON file (json) that provides the same documentation in a structured, machine-readable format. This format is useful for integration with other systems or for further automated processing.

## Installation

    git clone https://github.com/yourusername/MockOrderDataGenerator.git

    pip install pandas faker hypothesis sqlalchemy


## Usage

from saas_partner_order_generator import SaasPartnerOrderGenerator, OrderGenerator

strategy = SaasPartnerOrderGenerator()


## Dependencies

    pandas: For data manipulation and DataFrame support.
    
    Faker: For generating random data like names and addresses.
    
    hypothesis: For defining strategies to generate test data.
    
    openstreetmap-api: Custom API wrapper to fetch and handle OpenStreetMap data.
    
    sqlalchemy: (Optional) If you want to save the generated data to a database.

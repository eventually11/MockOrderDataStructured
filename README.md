# Partner Order Generator
This project is a Python-based tool designed to generate synthetic data for SaaS partner orders. The data can be used for testing, analysis, and validation purposes. It leverages libraries such as hypothesis for generating realistic test data, Faker for creating random data, and integrates with OpenStreetMap API to provide realistic addresses.

## Introduction
The Order Generator is a tool that automates the creation of order data. This can be especially useful for developers, data analysts, and QA teams to simulate real-world data for testing and development purposes.

## Features
Generate random order data with various attributes like order_id, tenant, flow, sender, service_fee, etc.

## Installation

pip install pandas faker hypothesis openstreetmap-api sqlalchemy


## Usage

from saas_partner_order_generator import SaasPartnerOrderGenerator, OrderGenerator

strategy = SaasPartnerOrderGenerator()


## Dependencies

    pandas: For data manipulation and DataFrame support.
    
    Faker: For generating random data like names and addresses.
    
    hypothesis: For defining strategies to generate test data.
    
    openstreetmap-api: Custom API wrapper to fetch and handle OpenStreetMap data.
    
    sqlalchemy: (Optional) If you want to save the generated data to a database.

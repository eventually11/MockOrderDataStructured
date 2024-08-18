# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:31:44 2024

@author: Administrator
"""

import yaml
import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)
from MockOrderDataStructured.saas_partner_order_structure import SaasPartnerOrderDataStructure

def load_config(config_file):
    """
    Loads the configuration from a YAML file.

    Parameters
    ----------
    config_file : str
        The path to the configuration file.

    Returns
    -------
    dict
        The loaded configuration settings.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration settings
    config = load_config('../config/config.yaml')
    
    structure = SaasPartnerOrderDataStructure()
    structure.generate_documentation(config['output_directory'])
    print("Documentation generated and saved to 'SaasPartnerOrderDataStructure_Documentation.txt'")


if __name__ == "__main__":
    main()
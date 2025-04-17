import os #Lets us work with folders and files
import sys #Helps track errors and system info
import numpy as np #Used for working with arrays and numeric data
import dill #Used to save and load Python objects like models or transformers
import yaml #Used to read and write setting files
from pandas import DataFrame #Used to label a table of data in function inputs

#Custom code for logging and error messages
from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.logger import logging

def read_yaml_file(file_path: str) -> dict:
    """
    Opens a YAML file and loads the data.

    Args:
        file_path (str): The location of the YAML file on the computer.
    
    Returns:
        dict: A dictionary that holds the values from the YAML file.
    """
    try:
        #Open the file in read mode and load its contents
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    #If something goes wrong, raise a detailed error message
    except Exception as e:
        raise custom_exception(e, sys) from e


#Max recommended lengths of code (79 and 72 for docstrings)
###############################################################################
########################################################################
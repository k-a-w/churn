#NEED to add comments and docstrings after class

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

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Saves a dictionary (or other Python object) into a YAML file.

    Args:
        file_path (str): Where the file should be saved.
        content (object): The data to write (like a dictionary).
        replace (bool): If True, deletes the file (if it already exists).
    """
    try:
        #Deletes the file if it both exists and the replace parameter = True
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        #Checks the folder where the file will be saved exists
        os.makedirs(os.path.dirname(file_path), exist_ok = True)

        #Writes the content to the YAML file
        with open(file_path, 'w') as file:
            yaml.dump(content, file)

    except Exception as e:
        raise custom_exception(e, sys) from e

def load_object(file_path: str) -> object:
    """
    Opens ... 
    """
    #NEED to add doc string here
    logging.info("Entered the load_object method of utils")

    try:
        #Open the file and load the object from it
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        
        logging.info("Exited the load_object method of utils")
        return obj
    
    except Exception as e:
        raise custom_exception(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array):
    """
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    
    except Exception as e:
        raise custom_exception(e, sys) from e

#MISSING load_numpy_array_data method here (Slide 13 has save numpy a second time)

def save_objects(file_path: str, obj: object) -> None:
    """
    """
    #NEED to add doc string here
    logging.info("Entered the save_object method of utils")

    try:
        #
        os.makedirs(os.path.dirname(file_path),exist=True)

        with open(file_path, "wb") as file_obj:
            obj = dill.dump(obj,file_obj)
        
        logging.info("Exited the save_object method of utils")
        return obj
    
    except Exception as e:
        raise custom_exception(e, sys) from e
    
def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    """
    logging.info("Entered the drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        return df
    
    except Exception as e:
        raise custom_exception(e, sys) from e

#Max recommended lengths of code (79 and 72 for docstrings)
###############################################################################
########################################################################
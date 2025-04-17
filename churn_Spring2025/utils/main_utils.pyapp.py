import os #Lets us work with folders and files
import sys #Helps track errors and system info
import numpy as np #Used for working with arrays and numeric data
import dill #Used to save and load Python objects like models or transformers
import yaml #Used to read and write setting files
from pandas import DataFrame #Used to label a table of data in function inputs

#Custom code for logging and error messages
from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.logger import logging

###############################################################################

def read_yaml_file(file_path: str) -> dict:
    """
    Opens a YAML file and loads the data.

    Args:
        file_path (str): The location of the YAML file on the computer.
    
    Returns:
        dict: A dictionary that holds the values from the YAML file.
    """
#ASK IF I can play around with using .__name__ and decorators
#StackOverflow Discussion:
# https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
    logging.info("Entered the read_yaml_file method of utils")

    try:
        #Open the file in read-only & binary mode then load its contents
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
       
        logging.info("Exited the read_yaml_file method of utils")

    #If something goes wrong, raise a detailed error message
    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Saves a dictionary (or other Python object) into a YAML file.

    Args:
        file_path (str): Where the file should be saved.
        content (object): The data to write (like a dictionary).
        replace (bool): If True, deletes the file (if it already exists).
    """
########################################################################
    logging.info("Entered the write_yaml_file method of utils")
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
        
        logging.info("Exited the write_yaml_file method of utils")

    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def save_object(file_path: str, obj: object) -> None:
    """
    Saves a Python object (like a model or tool) to a file.

    Args:
        file_path (str): Where to save the file.
        obj (object): The object to be saved.

    Returns:
        None
    """
    logging.info("Entered the save_object method of utils")

    try:
        #Creates the folder if it does not exist
        os.makedirs(os.path.dirname(file_path),exist=True)

        #Save the object using dill
        with open(file_path, 'wb') as file_obj:
            obj = dill.dump(obj,file_obj)
        
        logging.info("Exited the save_object method of utils")
        return obj
    
    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def load_object(file_path: str) -> object:
    """
    Opens a saved Python object (e.g. a trained model) from a file.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        object: The object that was stored (e.g. model, settings, etc.)
    """

    logging.info("Entered the load_object method of utils")

    try:
        #Open the file and load the object from it
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        
        logging.info("Exited the load_object method of utils")
        return obj
    
    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Saves a NumPy array (like a table of numbers) to a file.
    
    Args:
        file_path(str): Where the file should be saved.
        array (np.array): The data to be saved.
    """
    try:
        #Find the folder path from the provided file path
        dir_path = os.path.dirname(file_path)
        
        #If the folder does not exist, create the folder
        os.makedirs(dir_path, exist_ok=True)

        #Open the file and write the array to the file in binary format
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    
    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Loads a NumPy array that was previously saved.

    Args:
        file_path (str): Where the file is located.

    Returns:
        np.array: The array data that was stored in the file.

    """
    try:
        #Open the file and load the array from the file
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    
    except Exception as e:
        raise custom_exception(e, sys) from e

###############################################################################

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Removes the column(s) in the list from the DataFrame.

    Args:
        df (DataFrame): The table of data with which you're working.
        cols (list): A list of the columns you want to remove.

    Returns:
        DataFrame: A new table without the dropped columns.
    """
    logging.info("Entered the drop_columns method of utils")

    try:
        #Drop the columns from the table
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        return df
    
    except Exception as e:
        raise custom_exception(e, sys) from e
    
###############################################################################
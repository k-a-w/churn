from churn_Spring2025.configuration.mongo_db_connection import MongoDBClient
from churn_Spring2025.constants import DATABASE_NAME
from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.logger import logging

import pandas as pd
import sys
from typing import Optional
import numpy as np

class TelcoData:
    """
    Class Name: TelcoData
    Description: This class is responsible for extracting data from 
        MongoDB and converting the data into a DataFrame.

    Output: DataFrame containing the data from the MongoDB collection
    On Failure: Raises Exception with a custom error message
    """

    def __init__(self):
        """
        Initialize the MongoDB client and set the database name.
        """
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
            logging.info("MongoDB client initialized successfully.")
        except Exception as e:
            raise custom_exception(e, sys) from e
    
    def extract_data(self, collection_name: str, db_name: 
                     Optional[str]) -> pd.DataFrame:
        """
        Extract and convert data from MongoDB collection into a DataFrame.

        Args:
            collection_name (str): The name of the MongoDB collection 
                from which to extract data.
            database_name (Optional[str]): The name of the MongoDB 
                database. If None, use the collection_name.
        
        Returns:
            pd.DataFrame: A DataFrame containing the extracted data.
        """

        try:
            logging.info(f"Exporting data form collection: {collection_name}")

            if db_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[db_name][collection_name]
            
            data = list(collection.find())
            logging.info(f"Number of records extracted: {len(data)}")

            df = pd.DataFrame(data)
            logging.info(f"DataFrame shape before processing {df.shape}")

            if df.empty():
                logging.warning("No data found in the {collection_name} collection.")
                return df
            if "_id" in df.columns:
                df = df.drop(columns=["_id"], axis = 1)
                logging.info("Dropped the _id column from the DataFrame.")
            
            df.replace({"na": np.nan}, inplace=True)
            logging.info(f"DataFrame shape after processing {df.shape}")
            return df
        
        except Exception as e:
            raise custom_exception(e, sys)
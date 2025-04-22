import sys
import os
import pymongo

from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.logger import logging

from churn_Spring2025.constants import DATABASE_NAME, MONGODBURL

class MongoDBClient:
    """
    Class Name: MongoDBClient
    Description: This class is responsible for creating a MongoDB client and connecting to the database

    Output: Connection to the MongoDB Database
    On Failure: Raises Exception with a custom error message
    """
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODBURL)
                if mongo_db_url is None:
                    raise Exception("MONGODB_URL environment variable not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                logging.infor(f"MongoDB client created with URL: {mongo_db_url}")
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise custom_exception(e, sys) from e
        


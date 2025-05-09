import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from churn_Spring2025.constants import *

from churn_Spring2025.entity.config_entity import DataIngestionConfig
from churn_Spring2025.entity.artifact_entity import DataIngestionArtifact

from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.logger import logging

from churn_Spring2025.db_access.db_extract import TelcoData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = 
                 DataIngestionConfig()):
        """
        Args:
            data_ingestion_config: Configuration for data ingestion.
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise custom_exception(e, sys)

    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        Description: This method exports data from MongoDB to a csv file.

        Output: data is returned as artifact of a data ingestion component
        On Failure: write an exception log and then raise a custom exception
        """
        
        try:
            logging.info("Exporting data from MongoDB.")
            telco_data = TelcoData()
            #Changed telco_data.export_collection_to_dataframe(
            #--5/8/2025 1:31 pm
            dataframe = telco_data.extract_data(collection_name 
                            = self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving exported data into feature store at \
                         {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise custom_exception(e, sys)
    
    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        Description: split the dataframe into train and test based 
            on split ratio

        Output: folder created in s3 bucket with train and test data
        On Failure: write an exception log and then raise a custom exception
        """
        ratio = self.data_ingestion_config.train_test_split_ratio
        filepath_train = self.data_ingestion_config.training_file_path
        filepath_test = self.data_ingestion_config.testing_file_path
        
        try:
            if dataframe.empty:
                raise ValueError(MSG_DF_EMPTY)
            
            train_set, test_set = train_test_split(dataframe, test_size = ratio)
            logging.info(f"Performed the train test split with ratio: {ratio}")
            logging.info(f"Train set shape: {train_set.shape}")
            logging.info(f"Test set shape: {test_set.shape}")
            logging.info("Exiting the split_data_as_train_test method of Data_Ingestion class.")

            dir_path = os.path.dirname(filepath_train)
            os.makedirs(dir_path, exist_ok = True)

            logging.info(f"Exporting train data to {filepath_train} and \
                         test data to {filepath_test}")
            train_set.to_csv(filepath_train, index = False, header = True)
            test_set.to_csv(filepath_test, index = False, header = True)

            logging.info(f"Train and test data exported successfully.")

        except Exception as e:
            raise custom_exception(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Description: This method initiates the data ingestion process.

        Output: The train set and test set are returned as artifact of a data 
            ingestion component.
        On Failure: Write an exception log and then raise a custom exception.
        """
        filepath_train = self.data_ingestion_config.training_file_path
        filepath_test = self.data_ingestion_config.testing_file_path

        logging.info("Entering the initiate_data_ingestion method of " \
                    "Data_Ingestion class.")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Data exported from MongoDB.")

            if dataframe.empty:
                raise ValueError(MSG_DF_EMPTY)
            
            self.split_data_as_train_test(dataframe)
            logging.info("Data split into train and test sets.")

            logging.info("Exiting the initiate_data_ingestion method of the " \
                        "Data_Ingestion class.")
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path = filepath_train,
                test_file_path=filepath_test
            )
            logging.info(f"Data ingestion artifact created: {data_ingestion_artifact}.")
            return data_ingestion_artifact
        except Exception as e:
            raise custom_exception(e, sys) from e
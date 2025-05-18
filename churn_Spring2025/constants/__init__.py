#File that holds all of our constants (names of things)
import os
from datetime import date

DB_NAME = "DB_NAME" #Schema
COLLECTION_NAME = "telco_data" #Name of the table
MONGO_DB_URL = "MONGO_DB_URL" #Might need to be "MONGODB_URL"

PIPELINE_NAME:str = "telco_churn_pipeline"
ARTIFACT_DIR:str = "artifacts"

MODEL_FILE_NAME = "model.pkl"

#If it were live data, we would need to update duration (if we changed the tenure)

TARGET_COLUMN = "Churn"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessor.pkl"

FILE_NAME:str = "telco_churn.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


"""
Repeated error messages
"""
MSG_DF_EMPTY = "The dataframe is empty. Please check the " \
                "data loading process."

"""
Data Ingestion related constants with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME:str = "telco_data" #same as above
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation related constants with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
#uses package called evidently

"""
Data Transformation related constants with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "tranformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "transformed_object"

"""
MODEL TRAINER related constants with MODEL_TRAINER VAR NAME
"""
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config","model.yaml")

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "churn-model-evaluation-bucket"
MODEL_PUSHER_S3_KEY = "model-registry"

AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

APP_HOST = "98.81.96.0" #updated to 127.0.0.1 on 5/9
#changed again to 0.0.0.0 based off Fall 2024 project
#changing to instance to see if that will make things work
APP_PORT = 8080
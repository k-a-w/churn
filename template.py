import os #handles filepaths and creates files
from pathlib import Path

project_name = "churn_Spring2025"

#this template will allow us to use it for other projects
# so we're going to make a list of files

list_of_files = [
    f"{project_name}/__init__.py", #creates main project file
    #using constructor function so we can treat things as library storage
    #contains all the diff stages
    f"{project_name}/components/__init__.py", #holds all of the stages of ML pipeline
    f"{project_name}/components/data_ingestion.py", #get from MongoDB
    f"{project_name}/components/data_validations.py", #check for missing values, outliers, check structure and storage of data
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py", #where we figure out which model (best base model); potentially do hyper parameter training here
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py", #send our saved model to storage (S3 Bucket in this case)

    f"{project_name}/configuration/__init__.py", #allows import/export to this folder

    f"{project_name}/constants/__init__.py", #store values that don't change (mostly filepaths)

    f"{project_name}/entity/__init__.py", #entity in this case meaning the result of our work
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exceptions/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/util/__init__.py",



]
#Notes from class:
"""
What do the terms entity and artifact mean?
    Entity generally refers to some sort of core concept or object (e.g.
    data set or model); any significant conponents where managing and 
    tracking is beneficial.

    An artifact is typically a byproduct or result of the workflow (e.g.
    trained models, processed data sets, or evaluation reports).

The configuration refers to the settings and parameters which control
    how the code and model runs (e.g. hyperparameters for training, 
    filepaths, environment variables).
"""

from dataclasses import dataclass #allows use of decorators

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    metric_artifact:ClassificationMetricArtifact
    """
    is_model_accepted: bool
    changed_accuracy: float
    s3_model_path: str
    trained_model_path: str
    """

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool
    changed_accuracy: float
    s3_model_path: str
    trained_model_path: str

@dataclass
class ModelPusherArtifact:
    bucket_name: str
    s3_model_path: str
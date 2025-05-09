from churn_Spring2025.cloud_storage.aws_storage import SimpleStorageService
from churn_Spring2025.exceptions import custom_exception
from churn_Spring2025.entity.estimator import TelcoModel
import sys
from pandas import DataFrame

class TelcoEstimator:
    """
    This class is used to save and retrieve the model in s3 bucket and to do prediction
    """

    def __init__(self, bucket_name,model_path):
        """
        :param bucket_name: Name your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.s3 = SimpleStorageService()
        self.model_path = model_path
        self.loaded_model:TelcoModel=None
    
    def is_model_present(self, model_path):
        try:
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except custom_exception as e:
            print(e)
            return False
    
    def load_model(self)->TelcoModel: #has comma after self?
        """
        Load the model from the model_path
        :return:
        """
        return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)
    
    def save_model(self, from_file, remove:bool=False)->None:
        """
        Save the model to the model_path.
        :param from_file: Your local system model path
        :param remove: By default it is false (meaning you will have your model locally
        avaiable in your system folder)
        :return:
        """

        try:
            self.s3.upload_file(from_file, 
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise custom_exception(e, sys)
        
    def predict(self, dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise custom_exception(e, sys)
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.initiate_data_transformation()
        except Exception as e:
            raise e
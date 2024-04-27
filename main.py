from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from textSummarizer.logging import logging


#Data Ingestion Stage
# logging.info(f"Performing Data Ingestion Stage")
# data_ingestion_pipe = DataIngestionPipeline()
# data_ingestion_pipe.main()
# logging.info(f"Data Ingestion is Done Successfully")


#Data Validation Stage
logging.info(f"Data validation stage starts")
data_validation_pipe = DataValidationPipeline()
data_validation_pipe.main()
logging.info(f"Data Validation is Done Successfully")

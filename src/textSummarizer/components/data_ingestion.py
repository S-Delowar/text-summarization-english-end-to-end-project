import urllib.request as request
import zipfile
import os
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logging

class DataIngestion:
    def __init__(self, config = DataIngestionConfig) -> None:
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename= self.config.local_data_file
            )
            logging.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logging.info(f"File already exist")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_path)
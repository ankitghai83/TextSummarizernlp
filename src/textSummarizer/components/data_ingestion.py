## To create the component for data ingestion
import os
import urllib.request as request ## to download the data from the url
import zipfile,py7zr
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downaload! with following info: \n{headers}")

        else:
            
            logger.info(f"file already exists of size: {get_size(path=Path(self.config.local_data_file))}")
            
            

    def extract_zip_file(self):

        """zip_file_path:str
        Extract the zip file into the directory
        Function return None"""
        try:
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with py7zr.SevenZipFile(Path(self.config.local_data_file),'r') as zip_ref:
            #with py7zr.ZipFile(Path(self.config.local_data_file),'r') as zip_ref:
             zip_ref.extractall(unzip_path)
        except zipfile.BadZipFile:
            print(f"Error: {unzip_path} is not valid zip file")

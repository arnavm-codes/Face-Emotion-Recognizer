import os
import zipfile
import gdown
# import shutil
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

#################################################################################################################

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
 
################################################################################################################# 
        
    def download_file(self) -> str:
        """Fetch data from url"""
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok = True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
            
        except Exception as e:
            logger.error(f"Error during file download : {str(e)}")
            raise e   
   
#################################################################################################################  
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data directory
        Function returns None
        """         
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
#################################################################################################################     
     
#     def cleanup_unzip_dir(self):
#         """
#         Deletes the unwanted 'images/' folder inside unzip_dir if it exists.
#         """
#         unzip_path = self.config.unzip_dir
#         top_images_dir = os.path.join(unzip_path, "images")
#         nested_images = os.path.join(top_images_dir, "images")

#         if os.path.exists(nested_images) and os.path.isdir(nested_images):
#             logger.info(f"Deleting nested redundant folder: {nested_images}")
#             shutil.rmtree(nested_images)
#             logger.info(f"Nested 'images/' folder removed from {top_images_dir}")
#         else:
#             logger.info(f"No nested 'images/' folder found in {top_images_dir}. Nothing to clean up.")
        

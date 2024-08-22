import os
import sys
import pandas as pd 
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','train.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
            logging.info("Entered the initiate_data_ingestion")
            try:
                df=pd.read_csv('notebook\data\stud.csv')
                logging.info('Data is read')

                os.makedirs(os.path.dirname((self.ingestion_config.train_data_path)),exist_ok=True)
                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
                logging.info('Folders for data is created')

                train_set,test_set= train_test_split(df,test_size=0.2,random_state=40)
                train_set.to_csv(self.ingestion_config.train_data_path_data_path,index=False,header=True)
                test_set.to_csv(self.ingestion_config.test_data_path_data_path,index=False,header=True)

                logging.info('Data is now train test split')

                return(
                     self.ingestion_config.train_data_path,
                     self.ingestion_config.test_data_path
                )
            except Exception as e:
                 raise CustomException(e,sys)
                 
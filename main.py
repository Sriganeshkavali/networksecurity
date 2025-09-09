from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.confing_entity import DataIngestionConfig,TrainingPipelineConfig

import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(TrainingPipelineConfig())
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate data ingestion")
        dayaingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dayaingestionartifact)
        logging.info("data ingestion completed")

        
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

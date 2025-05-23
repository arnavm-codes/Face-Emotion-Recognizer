from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stages ={
    "Data Ingestion Stage": DataIngestionTrainingPipeline    
}

#################################################################################################################

def run_stage(stage_name, pipeline_class):
    """Runs a pipeline stage with logging and exception handling."""
    try:
        logger.info(f">>>>>> stage {stage_name} has started <<<<<<")
        
        pipeline = pipeline_class()
        pipeline.main()
        
        logger.info(f">>>>>> stage {stage_name} has finished <<<<<<\n x==========x")
    
    except Exception as e:
        logger.exception(f"Error in {stage_name}: {e}")
        raise e

#################################################################################################################

"""Main Function"""    
def main():
    """Run all enabled pipeline stages."""
    for stage_name, pipeline_class in stages.items():
        run_stage(stage_name, pipeline_class) 
        
if __name__ == "__main__"  :
    main()       
        
        
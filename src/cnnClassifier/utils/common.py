import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from cnnClassifier import logger
import json
import joblib
from pathlib import Path
import base64
from typing import any
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns
    
    Args:
        path_to_yaml(str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type        
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e    
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) :
    """create list of directories
    
    Args: 
        path_to_directories(list) : list of  path to directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to False
    """ 
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")
    

@ensure_annotations
def save_json(path:Path, data: dict):
    """save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")    
    
    
@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    """loads json file data
    
    Args:
        path(Path): path to json file
        
    Returns:
        ConfigBox:  data as class attributes instead of dict    
    """
    with open(path) as f:
        content = json.load(f)
         
    logger.info(f"json file is loaded successfully from {path}")
    return ConfigBox(content)    
    
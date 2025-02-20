import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations ## type: ignore
from box import ConfigBox ## ConfigBox is a type that allows you to access the dictionary keys as attributes
from pathlib import Path
from typing import Any

## Reading the yaml file and returning my YAML file as  ConfigBox type
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and return a ConfigBox object
    Args:
        path_to_yaml (str): Path like input
    Raises:
        Value Error: If the file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError(f"Empty file: {path_to_yaml}")
    except Exception as e:
        raise e
    

## Method to Create a directory
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """Create directories
    Args:
        path_to_directories (list): List of path of directories
        ignore_log (bool, optional): Ignore if multiple dir need to be created.Default is False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")


## Method to get the size of the file
@ensure_annotations
def get_size(path:Path) -> str:
    """ Get size in KB
    Args:
        path (Path): Path of the file
    returns:
        str: Size of the file
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"



    
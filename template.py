import os
from pathlib import Path
import logging

## Setting up logging basic configuration
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s') ## log string format
## .github folder is created for github actions during CI CD deployment and create CI CD .yaml file, when we do the commit in github it will automaticall take code to the cloud and deploy it.
## .gitkeep file is created to keep the folder structure in the github repository and that allow to upload empty folder to the github repository.
project_name = 'textSummarizer'
list_of_files = [".github/workflows/.gitkeep/",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/logging/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "params.yaml",
                 "app.py",
                 "main.py",
                 "Dockerfile",
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb"]## In config.yaml file we will keep all the configuration details of the project anfd in params.yaml we have all the parameters of the models.Docker is used to create the docker image of the source code and do deployments in AWS EC2.setup.py is used  to setup the python local package and install it in the system.

##trials.ipynb is used to do the research and development of the using jupyter notebook to do all the experiments



## Logic to create all above files and folders
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
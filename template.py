import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO  , format='[%(asctime)s]: %(message)s')

project_name = "textsummarizer"

list_of_files = [
     ".github/workflow/.gitkeep",
     f"src/{project_name}/__init__.py",
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utilities/__init__.py",
     f"src/{project_name}/utilities/common.py",
     f"src/{project_name}/logging/__init__.py",
     f"src/{project_name}/config/__init__.py",
     f"src/{project_name}/config/configuration.py",
     f"src/{project_name}/pipeline/__init__.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/constant/__init__.py",
     "config/config.yaml",
     "params.yaml",
     "app.py",
     "main.py",
     "Dockerfile",
     "requirements.txt",
     "setup.py",
     "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating a Directory : {filedir} for the File {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f :
            pass
            logging.info(f"Creating Empty File : {filepath}")

    else : 
        logging.info(f"{filepath} Already Exists")



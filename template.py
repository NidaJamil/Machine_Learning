from pathlib import Path
import logging
import os

logging.basicConfig(level=logging.INFO)

project_name= "mlproject"

##use to create git folder that will use in deployement
list_of_files=[
     ##".github/workflows/.gitkeep",
     f"src/{project_name}/__init__.py",
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/components/data_ingestion.py", 
     f"src/{project_name}/components/data_transformation.py", 
     f"src/{project_name}/components/model_training.py",
     f"src/{project_name}/components/model_monitoring.py",
     f"src/{project_name}/pipline/__init__.py",
     f"src/{project_name}/pipline/training_pipline.py",
     f"src/{project_name}/pipline/prediction_pipline.py",
      ##fils for esxception handling, logging, utils
     f"src/{project_name}/exception.py",
     f"src/{project_name}/logger.py",
     f"src/{project_name}/utils.py",
     "app.py",
     "Dockerfile",
     "requirement.txt",
     "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file{filename}")   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"create empty file: {filepath}")


    else:
        logging.info(f"{filepath} is already exist")



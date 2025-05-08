import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "networkSecurity"

list_of_files = [
    ".github/workflows/.gitkeep",
    "Network_Data/.gikeep",
    f"{project_name}/__init__.py",
    f"{project_name}/cloud/__init__.py",
    f"{project_name}/cloud/s3_synchronizer.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training_pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/logging/logger.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/batch_prediction.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils/__init__.py",
    f"{project_name}/utils/main_utils/utils.py",
    f"{project_name}/utils/ml_utils/__init__.py",
    f"{project_name}/utils/ml_utils/metric/__init__.py",
    f"{project_name}/utils/ml_utils/metric/classification_metric.py",
    f"{project_name}/utils/ml_utils/model/__init__.py",
    f"{project_name}/utils/ml_utils/model/estimator.py",
    ".env",
    "Notebook/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filename)  == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty File: {filename}")
    
    else:
        logging.info(f"{filename} is already Created")
import os
from pathlib import Path
import logging

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "main.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "research/trails.ipynb"
]


for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating filepath: {filepath}")
    else:
        logging.info(f"{filename} is already exist")

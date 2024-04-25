import yaml
import os
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from ensure import ensure_annotations
from textSummarizer.logging import logging



@ensure_annotations
def read_yaml_file(file_path):

  try:
    with open(file_path) as file:
      data = yaml.safe_load(file)
      logging.info(f"yaml file- {file_path} is loaded successfully")
      return ConfigBox(data)
  except BoxValueError:
      raise ValueError("yaml file is empty")
  except Exception as e:
      raise e
#   except FileNotFoundError:
#     raise FileNotFoundError(f"YAML file not found: {file_path}")
#   except yaml.YAMLError as e:
#     raise YAMLError(f"Error parsing YAML file: {e}")



def create_directories(paths: list):
  for path in paths:
    try:
      os.makedirs(path, exist_ok=True)  # Create directories recursively, ignoring existing ones
      print(f"Directory created: {path}")
    except OSError as e:
        print(f"Error creating directory: {path} - {e}")
        raise e
        
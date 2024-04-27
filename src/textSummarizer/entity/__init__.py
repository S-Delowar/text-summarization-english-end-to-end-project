from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path
    
@dataclass
class DataValidationConfig:
    root_dir : Path
    status_file : str
    all_required_files : list
    
@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    tokenizer_name : Path
    transformed_data_path : Path

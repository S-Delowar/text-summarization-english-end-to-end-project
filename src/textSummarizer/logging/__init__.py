import logging
import os
from datetime import datetime

log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logging_str = f"[%(asctime)s %(levelname)s %(name)s %(module)s %(lineno)d - %(message)s]"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok= True)

log_file_path = os.path.join(logs_dir, log_file_name)

logging.basicConfig(
    # filename=log_file_path,
    level=logging.INFO,
    format= logging_str,
    handlers= [
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)
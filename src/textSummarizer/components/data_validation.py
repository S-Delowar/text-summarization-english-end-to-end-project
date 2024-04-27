from textSummarizer.entity import DataValidationConfig
import os

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        self.config = config
    
    def validate_all_data_exist(self):

        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            
            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validation status: {validation_status}")
        except Exception as e:
            raise e
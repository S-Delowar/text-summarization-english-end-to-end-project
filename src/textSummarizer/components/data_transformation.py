from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    def convert_text_to_features(self, text_batch):
        input_encodings = self.tokenizer(text_batch['dialogue'], max_length = 1024, truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(text_batch['summary'], max_length = 128, truncation = True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }    

    def initiate_data_transformation(self):
        data = load_from_disk(self.config.data_path)
        data_pt = data.map(self.convert_text_to_features, batched= True)
        data_pt.save_to_disk(self.config.transformed_data_path)
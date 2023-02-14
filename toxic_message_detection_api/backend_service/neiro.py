import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Neiro:
    '''Детекция токсичных сообщений с помощью BERT'''
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("s-nlp/russian_toxicity_classifier")
        self.model = AutoModelForSequenceClassification.from_pretrained("s-nlp/russian_toxicity_classifier")

    def predict(self, message: str) -> str:
        inputs = self.tokenizer(message, return_tensors="pt")

        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        answer = self.model.config.id2label[predicted_class_id]

        return answer
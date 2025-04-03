# pip install transformers torch

from transformers import AutoModelForSequenceClassification, AutoTokenizer

#Choice model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# download
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# saving model locally 
model.save_pretrained("models/")
tokenizer.save_pretrained("models/")

print("✅ Model downloaded and saved to 'models/'")
from transformers import pipeline





# run model
# classifier = pipeline("sentiment-analysis", model="models/", tokenizer="models/")

# simple test
# result = classifier("I love this project!")
# print(result)  # Output： [{'label': 'POSITIVE', 'score': 0.9998}]

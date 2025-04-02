#predict.py
from transformers import pipeline


classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]  # get result of analysis
    return {"text": text, "sentiment": result['label'], "score": result['score']}

if __name__ == "__main__":
    text = "I love this product!"
    print(analyze_sentiment(text))

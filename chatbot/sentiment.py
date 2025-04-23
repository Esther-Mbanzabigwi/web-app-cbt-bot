from transformers import pipeline
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    return result['label'], result['score']

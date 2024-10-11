from transformers import pipeline

# Initialize the sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis')

def analyze_sentiment(sentiments):
    results = classifier(sentiments)
    positive_count = sum(1 for result in results if result['label'] == 'POSITIVE')
    negative_count = len(results) - positive_count

    return {
        'positive': positive_count,
        'negative': negative_count
    }

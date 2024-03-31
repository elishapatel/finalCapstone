import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from textblob import TextBlob

# Load the dataset
data = pd.read_csv('amazon_product_reviews.csv')

# Load the larger spaCy model
nlp = spacy.load('en_core_web_md')

# Create a function that preprocess the text data
def preprocess_text(text):
    # Remove stopwords and punctuation
    stop_words = STOP_WORDS  # cleaner code than using .is_stop
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if token.text.lower() not in stop_words and not token.is_punct]
    
    # Join tokens into a string
    clean_text = ' '.join(tokens)
    
    return clean_text

# Create a function for sentiment analysis
def analyse_sentiment(review):
    # Preprocess the review text
    clean_review = preprocess_text(review)
    
    # Analyse sentiment using TextBlob
    blob = TextBlob(clean_review)
    polarity = blob.sentiment.polarity
    
    # Classify sentiment based on polarity score
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Test the sentiment analysis function
def test_sentiment_analysis():
    for i in range(2):
        review = data['reviews.text'][i]
        print(f"\nSample Review {i + 1}:", review)
        print("Sentiment:", analyse_sentiment(review))

# Compare similarity of two reviews
def compare_similarity(review1, review2):
    review1 = nlp(preprocess_text(review1))
    review2 = nlp(preprocess_text(review2))
    similarity = review1.similarity(review2)
    print(f"\nSimilarity between Review 1 and Review 2: {similarity}")

# Test the sentiment analysis function
test_sentiment_analysis()

# Compare similarity of two reviews
compare_similarity(data['reviews.text'][0], data['reviews.text'][1])
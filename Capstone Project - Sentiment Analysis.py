# Importing spacy and the en_core-web_sm model as well as the Pandas library to pre-process the data.
import spacy
nlp = spacy.load('en_core_web_sm')
import pandas as pd


# Importing the Amazon Customer Reviews data, storing it in a df variable and stripping it off any missing reviews.
df = pd.read_csv('amazon_product_reviews.csv')
reviews = df.dropna(subset=['reviews.text'])


# Applying spaCy to each review to remove any stopwords, then joining the tokens - Having the text as a string to easily feed it into the model.
review_tokens = []
for text in reviews['reviews.text']:
    tokens = [token.text for token in nlp(text) if not token.is_stop]
    review_tokens.append(' '.join(tokens))


# Importing TextBlob
from textblob import TextBlob


# Analysing sentiment for each review
for review in review_tokens:
    # Calculating polarity using TextBlob
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    # Assigning sentiment label based on the polarity
    sentiment_label = 'POSITIVE' if polarity >= 0 else 'NEGATIVE' if polarity < 0 else 'NEUTRAL'

    print(f"Review: '{review}'")
    print(f"Polarity: {polarity}")
    print(f"Sentiment: {sentiment_label}")
    print("\n")

# Data_Science_Bootcamp-Capstone_Project_2_Sentiment_Analysis

The dataset l utilised for this project is Amazon’s customer reviews on kaggle.com. The dataset includes basic product information, rating, review text, and more for each product.

The preprocessing steps involve things like tokenization, this is splitting the text into individual words or tokens. Eliminating common words that do not contribute much to sentiment analysis. Reducing words to their base or root form for better analysis.

The sentiment analysis using spaCy's model and the “.sentiment” attribute appears to result in neutral sentiment for the provided reviews. This changes however, when using the TextBlob library, which includes the .polarity attribute, the sentiment polarity (positive, negative, or neutral) can be obtained. I think without using the TextBlob library I’d struggle to successfully execute the task.

SpaCy provides powerful natural language processing capabilities, including tokenization, lemmatization, and sentiment analysis. The spaCy model's sentiment analysis might not be capturing sentiment nuances effectively, as all reviews were classified as neutral. This could also be because of my code, however I did get it to work with TextBlob.

The model successfully demonstrated effectiveness in capturing sentiment from diverse product reviews as well as robustness in handling different writing styles and language nuances. I do believe that the model may struggle with things like sarcasm or context-heavy reviews. Finally everything is heavily dependent on data quality: The model’s performance depends on and counts on the quality and representativeness of the training data.

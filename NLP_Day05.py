from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "NLP is great",
    "NLP is fun",
    "NLP is amazing"
]

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Transform documents into BoW matrix
bow_matrix = vectorizer.fit_transform(documents)

# Display the vocabulary
print("Vocabulary:", vectorizer.vocabulary_)

# Convert to array for better readability
print("BoW Matrix:\n", bow_matrix.toarray())

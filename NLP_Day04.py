import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer=WordNetLemmatizer()
words=['Flying','kicking','singing','jumping']

print('Lemmatized_Words:', [lemmatizer.lemmatize(word, pos="v")for word in words])
import nltk
from nltk.stem import PorterStemmer

stemmer =PorterStemmer()

words=['cycling','swimming','drawing','bathing']
stemmed_words=[stemmer.stem(word) for word in words]
print('stemmed words: ',stemmed_words)
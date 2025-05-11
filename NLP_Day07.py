import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
sentence = 'The quick brown fox jumps over the lazy dog'

# Tokenize and POS tag
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens, lang='eng') 

print('POS tags:', pos_tags)

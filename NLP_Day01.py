import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
text='Don is back, He is ready to conquer the whole world'

sentences=sent_tokenize(text)
print('sentences: ',sentences)

words=word_tokenize(text)
print('words: ',words)
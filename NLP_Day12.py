from textblob import TextBlob
text="I Absolutely love you. Your are Fantastic my Love!"
blob=TextBlob(text)
print('sentiment:',blob.sentiment.polarity)
# The sentiment of the text is calculated using TextBlob
print('sentiment:',blob.sentiment.subjectivity)
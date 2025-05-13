from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

text=['I love programming in Python',
      'Python is not a good language',
      'I hate programming in Java',
      'Java is a good language',]
labels=['positive','negative','negative','positive']

model=make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(text,labels)
# The model is trained on the text and labels provided above
test=['I love Python programming in Java']
prediction=model.predict(test)
print('Predicted_Text:',prediction[0])
# The model predicts the sentiment of the test text
# The predicted sentiment is printed

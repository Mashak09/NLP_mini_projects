from sklearn.feature_extraction.text import TfidfVectorizer
#skcitlearn-ml library,feature_extracation: converts text to numbers and tfid vectorizer tf-idf to convert text into numbers

documents=['DON is back','Is DON really Back', 'Yes DON is really back']

tfid_vectorizer=TfidfVectorizer()
#intitializing TfidfVectorizer

tfidf_matrix= tfid_vectorizer.fit_transform(documents)
#converts the text into matrix form using the tranform 

print('Vocabulary: ',tfid_vectorizer.vocabulary_)

print('tfidf_matrix.\n',tfidf_matrix.toarray())
#convert the matrix into an array an array of numbers bcz its easier to read

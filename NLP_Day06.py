import gensim.downloader as api  # Import the downloader
#importing gensim library which as pre-trained models like word2vec

# Load the pre-trained Word2Vec model (may take time and space)
model = api.load('word2vec-google-news-300')
#loads and downloads word2vec-google-news which is trained on google news

similar_words = model.most_similar('king', topn=5)
#asks the model which words are most similar to king and asks top 5 words
print("Words similar to 'king':", similar_words)

result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
#adds king and woman and subtracts man to give word similar
print("king - man + woman ≈", result)

glove_model=api.load('glove-twitter-50')
#this loads and downloads model trained on twitter-50 words
print("word similar to 'happy':",glove_model.most_similar('happy',topn=5))

fasttext_model=api.load("fasttext-wiki-news-subwords-300")
print("words most similar to 'computer':",fasttext_model.most_similar('computer',topn=5))
print("Words most similar to 'compuetr' (misspelled 'computer'):", fasttext_model.most_similar('compuetr', topn=5))

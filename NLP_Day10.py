import spacy
#nlp library used for tokenization, part-of-speech tagging, named entity recognition, and dependency parsing
nlp=spacy.load("en_core_web_sm")
text="The cat sat on the mat."
#nlp object is created by loading the small English language model    
doc=nlp(text)
#doc object is created by processing the text with the nlp object
for token in doc:
    print(f"{token.text} \u2192 {token.dep_} \u2192 {token.head.text}")

# The output shows the dependency relationship between each token and its head token.   
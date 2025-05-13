import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Example sentence
sentence = "The cat sat on the mat."

# Process sentence
doc = nlp(sentence)

# Print dependencies
for token in doc:
    print(f"{token.text} → {token.dep_} → {token.head.text}")

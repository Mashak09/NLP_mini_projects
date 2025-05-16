from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Natural Language Processing enables computers to understand human language.
It has many applications such as chatbots, translation, sentiment analysis, etc.
With the rise of large language models, NLP is evolving rapidly.
"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

summary_sentences = summarizer(parser.document, sentences_count=2)
for sentence in summary_sentences:
    print(sentence)

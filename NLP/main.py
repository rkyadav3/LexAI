import re
import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess(text):
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    return tokens

sample_text = "What are my rights if I get wrongfully terminated from my job?"
processed_text = preprocess(sample_text)
print(processed_text)

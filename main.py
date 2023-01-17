# import nltk
import json
from poemEntry import PoemEntry
from data import Data
from spacy.lang.fr import French

data = Data()

with open("poems.json","r") as file:
    dataJson = json.load(file)
    for poemEntryDict in dataJson:
        poemEntry = PoemEntry(poemEntryDict["title"], 
                              poemEntryDict["author"], 
                              poemEntryDict["poem"])
        data.poems.append(poemEntry)
        
# tokenizer = nltk.data.load('/home/phil/nltk_data/tokenizers/punkt/french.pickle')
# for poem in data.poems:
#     sentenceTokenEnumerator = tokenizer.tokenize(poem.poem)
#     sentences = [sentence for sentence in sentenceTokenEnumerator]
#     for sentence in sentences:
#         print(sentence)
#         wordTokenEnumerator = tokenizer._tokenize_words(sentence)
#         poem.tokens = [token for token in wordTokenEnumerator if token.tok not in string.punctuation]
#         for token in poem.tokens:
#             print(token)

nlp = French()
tokenizer = nlp.tokenizer
for poem in data.poems:
    tokens = tokenizer(poem.poem)
    for token in tokens:
        print(token)
    break
    
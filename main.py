import json
from poem import Poem
from data import Data
from spacy.lang.fr import French
import spacy

data = Data()

# loading the database
with open("poems.json","r") as file:
    dataJson = json.load(file)
    for poem in dataJson:
        poem = Poem(poem["title"], 
                              poem["author"], 
                              poem["poem"])
        data.poems.append(poem)
        
nlp = French() # spacy instance

# modifying the tokenizer to fit my needs
# suffixes = list(nlp.Defaults.suffixes)
# suffixes.remove("’") # removing ’ from the suffixes so that "j’ai" is one token
# suffixes.remove("-") # removing - from the suffixes so that "suis-je" is one token
# suffix_regex = spacy.util.compile_suffix_regex(suffixes)
# nlp.tokenizer.suffix_search = suffix_regex.search

# prefixes = list(nlp.Defaults.prefixes)
# prefixes.remove("’") # removing ’ from the prefixes so that "j’ai" is one token
# prefixes.remove("-") # removing - from the prefixes so that "suis-je" is one token
# prefix_regex = spacy.util.compile_prefix_regex(prefixes)
# nlp.tokenizer.prefix_search = prefix_regex.search

# tokenizing
for poem in data.poems:
    tokens = nlp.tokenizer(poem.poem)
    for token in tokens:
        if token.is_punct: # skip tokens that are only punctuation
            continue
        
        print(token)
    break
    
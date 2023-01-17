import json

class PoemEntry(object):
    def __init__(self, jsonDict):
        self.title = jsonDict["title"]
        self.author = jsonDict["author"]
        self.poem = jsonDict["poem"]
        self.tokens = []
    
    def __init__(self, title: str, author: str, poem: str):
        self.title = title;
        self.author = author;
        self.poem = poem;
        self.tokens = [];
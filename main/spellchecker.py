import json
import re

try:
    dictionary_data = open('main/dictionary.txt','r')
    
except OSError:
    print('!MISSING_DICTONARY , Run dictionary.py as python script.')

dictionary = json.load(dictionary_data)

class spellcheck():
    
    def get_words(self,line):
        
        # extract english words from the string

        return  re.findall(r'[a-zA-Z_\']+',line)

    def Scheck(self,line):
        suggestion = []
        self.words = [wrd.lower() for wrd in self.get_words(line)]
        for word in self.words:
            if word in dictionary:
                continue
            else:
                suggestion.append(word)   
        return suggestion
    

'''
Future Work:

Implementation of suggestion for misspelled words.
Autorcorrect the lines 
Ignore the errors
Add to dictionary

'''
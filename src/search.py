'''

This class contains the main search, we can parse our searchwords into a wordset,
cut the wordstem and lookup the word in our Cassandra


Created on 21.09.2011

@author: kq
'''
from re import finditer, compile
import database
from stemming.porter2 import stem

class search(object):

    def __init__(self):
        self.pattern = compile(r"[\b\w\b]{2,35}")    
        self.db = database.database()

    def parse_searchwords(self, query):
        out = set()
        for match in finditer(self.pattern, query):
            out.add(match.group(0).lower())
        print out
        return out

    def mk_wordstem(self, wordSet):
        out = set()
        for item in wordSet:
            out.add(stem(item))
        return out
    
    #if we get something like "foo + bar" we should only show documents with these words inside.
    '''
        {
            'word0' : ["docID00", "docID01"],
            'word1' : ["docID01", "docID0X"]
        }
        
        as result only return the following docid: docID01
        
        if our result looks like this:
        
        {
            'word0' : ["docID00","docID01","docID0X"],
            'word1' : ["docID01", "docID0X", "docID0F"]
        }
        return the following docids: docID01, docID0X
    '''
    def lookup(self, wordSet):
        resultset = dict()
        if type(wordSet) != type(set()):
            # query database with single word and save in dict()
            resultset = self.db.getSingleResult(wordSet)
            return resultset
        else:
            resultset = self.db.getResultset(wordSet)
            return resultset
        return dict()
        # query docids for paths
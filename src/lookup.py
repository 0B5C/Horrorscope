'''
Created on 26.09.2011

@author: kq
'''
import re
import database

# TODO: Implement counter in cassandra to count the words
# add and sub counter!!

class lookup(object):
    def __init__(self):
        self.pattern = re.compile(r"[\b\w\b]{2,35}")
        self.db = database.database()

    def splitAndTrigger(self, words):
        wordlist = set()
        for word in re.finditer(self.pattern, words):
            wordlist.add(word)
        lookup.boom(wordlist)

    def sort(self, wordlist):
        for word in wordlist:
            # get counts of words
            # sort word by occurance
            # return words
            pass
        pass

    def boom(self, wordlist):
        pass
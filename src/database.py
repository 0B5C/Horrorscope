'''
Created on 21.09.2011

@author: kq
'''
import pycassa
# TODO: Exceptionhandling
class database(object):
    def __init__(self):
        self.pool = pycassa.connect('indexer', ['194.9.127.241:9160'])
        self.col_fam_name = 'indexx'
        self.col_fam = pycassa.ColumnFamily(self.pool, self.col_fam_name)

    # words
    def getSingleResult(self, word):
        if self.col_fam_name == 'docids':
            self.col_fam_name = 'indexx'
        return self.col_fam.get(word)

    def getResultset(self, wordSet):
        if self.col_fam_name == 'docids':
            self.col_fam_name = 'indexx'
        #return self.col_fam.multiget(wordSet)
        return self.col_fam.multiget(wordSet)

    # lookup of docids
    def getSinglePath(self, uuid):
        if self.col_fam_name == 'indexx':
            self.col_fam_name = 'docids'
        return self.col_fam.get(uuid)

    def getPaths(self, uuidSet):
        if self.col_fam_name == 'indexx':
            self.col_fam_name = 'docids'
        return self.col_fam.multiget(list(uuidSet))
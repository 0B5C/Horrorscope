'''
Created on 21.09.2011

@author: kq
'''

import search

def main():
    worker = search.search()
    query = "physic"
    queryAsSet = worker.parse_searchwords(query)
    if queryAsSet == set([]):
        print "[ERROR] - The query string is not valid."
        return -1
    wordstems = worker.mk_wordstem(queryAsSet)
    result = worker.lookup(wordstems)
    print result
    exit()

if __name__ == '__main__':
    main()
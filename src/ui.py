'''
Created on 21.09.2011

@author: kq
'''

class ui(object):
    
    #wordSet should contain the words we want to highlight
    # we should highlight with html tags or something like that
    def highlight(self, wordSet):
        pass


    #documents is a list which contains our documents, the names of the document and the path to our document.
    '''
    Example input:
        {
            'document_text' : "Lorem ipsum <font color=\"red\">Dilorum</font>",
            'name'          : "Document_404.txt",
            'path'          : "/home/kq/documents"
        }
    '''
    def display(self, documents):
        pass
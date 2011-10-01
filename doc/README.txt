> The arachneSearch is a document based searchengine written for
  the arachneCrawler.
  It contains several options for searching through a created index
  of arachneCrawler on our cassandradatabase.
  
>> Web UI
>> Fulltextsearch
>> Wordstem lookup

Procedure:

Look for word
if found:
	get docid
	if docid != null:
		- look into database docids and get the real path of
		  a textdocument
		- display highlighted textfile

# cut search word to wordstem
# query database for wordstem
# query text for word
# use in highlighting the original word and only 
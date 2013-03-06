# Project: Search Engine
# Author: Santiago Paiva
# Version 1.0

#Extract Link function

def printAllLinks(s):
        while True: 
                url, endpos = getNextTarget(s)
                if url:
                        print url
                        s = s[endpos:]
                else:
                        break
                        

def getNextTarget(s):
	startLink = s.find('<a href=')

        #Tests whether no link was found
	if start_link == -1:
                return None, 0 
        startQuote = s.find('"', startLink)
        endQuote = s.find('"', startQuote + 1)
        url = s[startQuote + 1 : endQuote ]
        return url, endQuote


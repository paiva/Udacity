#
# Project: Python Search Engine
# Author: Santiago Paiva
# Version 1.0
#--------------------------------------------------------------

def getNextTarget(s):
        """returns the url and the position of the enquote"""
        
	startLink = s.find('<a href=')

        #Tests if no link was found
	if start_link == -1:
                return None, 0 
        startQuote = s.find('"', startLink)
        endQuote = s.find('"', startQuote + 1)
        url = s[startQuote + 1 : endQuote ]
        return url, endQuote

def getAllLinks(s):
        """returns a list of all the links found on a page.
                """

        links = [] 

        while True: 
                url, endpos = getNextTarget(s)
                if url:
                        #Collect a list of URLs found
                        links.append(url)
                        s = s[endpos:]
                else:
                        break
        return links                

# Project: Search Engine
# Author: Santiago Paiva
# Version 1.0

#Extract Link function
def getNextTarget(s):
	startLink = s.find('<a href=')
	startQuote = s.find('"', startLink)
	endQuote = s.find('"', startQuote + 1)
	url = s[startQuote + 1 : endQuote ]
	return url, endQuote
	
	
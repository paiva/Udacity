#------------------------------------------------------------------------
# Project: Python Search Engine
# Author: Santiago Paiva
# Version 1.0
# File: crawler.py
#------------------------------------------------------------------------

from bs4 import BeautifulSoup

def getPage(url):
    """
        Inputs a URL and ouputs the content of that URL
    """

    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    
def getAllLinks(page):
    """
        Implements BeautifulSoup module.
        Returns all links
    """
    soup = BeautifulSoup(page)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

##def getNextTarget(page):
##    """
##        Assummes that s is the seed page.
##        Returns the url and the position of the enquote.
##    """
##        
##    startLink = page.find('<a href=')
##
##    #Tests if no link was found
##    if startLink == -1:
##        return None, 0 
##    startQuote = page.find('"', startLink)
##    endQuote = page.find('"', startQuote + 1)
##    url = page[startQuote + 1 : endQuote ]
##    return url, endQuote

##def getAllLinks(page):
##    """
##        Takes seed page url as an input.
##        Returns a list of all the links found on a page.
##    """
##
##    links = [] 
##
##    while True: 
##        url, endpos = getNextTarget(s)
##
##        if url:
##            #Collect a list of URLs found
##            links.append(url)
##            s = s[endpos:]
##        else:
##            break
##    return links     

def splitString(source,splitlist):
    """
        inputs: the string to split and a string containing
        all of the characters considered separators. The
        procedure should return a list of strings that break
        the source string up by the characters in the
        splitlist.
    """
    output = []
    atsplit = True #At a split point

    for char in source:
        if char in splitlist:
            atplist = true
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #add character to last word
                output[-1] = output[-1] + char
    return output
                

           

def addPagetoIndex(index,url,content):
    """
        Inputs:
        -Index
        -URL (string)
        -Content (string)

        Updates the index to include all of the word occurences
        found in the page content by adding the url to the word's
        associated url list.
    """

    words = content.split()

    for word in words:
        addToIndex(index,word,url)
        

def addToIndex(index,keyword,url):
    """
        Inputs:
        - an index: [[keyword,[[url,count],[url,count],...]],...]
        - a keyword: String
        - a url: String
    """

    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def crawlWeb(seed,maxpages):
    """
        Takes seed page url as an input. Maxpages is used
        to stop crawling after we reach a certain amount of pages
        since it follows a Depth-first search approach. Outputs
        a list of all the URLs that can be reached by following
        links starting from the seed page

        Returns an index and a graph. The graph should be a
        Dictionary where the entries are url(page):[url,url,...]
    """

    tocrawl = set([seed])
    crawled = set() #len(crawled) is length of crawled
    index = {}
    graph = {}
    
    #While there are more pages to crawl
    while tocrawl:
         
        #Picks last page.
        page = tocrawl.pop()

        #Tests if page was already crawled
        if page not in crawled and len(crawled) < maxpages:

            content = getPage(page)
            #Adds all the link targets on this page to tocrawl
            addPagetoIndex(index,page,content)
            outlinks = getAllLinks(content)
            graph[page] = outlinks
            tocrawl.update(outlinks)
            #Adds the page to the list of crawled pages
            crawled.add(page)
    return index, graph

def computeRanks(graph):
    d = 0.8 #Damping Factor

    numloops = 10

    ranks ={}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0/npages
        
    for i in range(0,numloops):
        newranks = {}
        for page in graph:
            newrank = (1-d)/npages

            #Update by summing in the inlink ranks
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d*(ranks[node] / len(graph)) 
        newranks[page] = newrank
        ranks = newranks
    return ranks

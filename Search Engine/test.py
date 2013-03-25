### 
### test.py
###

import search
import crawler

def test_engine():
    print "Testing..."
    index, graph = crawler.crawl_web('http://udacity.com/cs101x/urank/index.html')
    ranks = crawler.compute_ranks(graph)
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'
    # print lucky_search(index, ranks, 'Hummus')
    assert search.lucky_search(index, ranks, 'Hummus') == kathleen
    #print ordered_search(index, ranks, 'Hummus')
    assert search.ordered_search(index, ranks, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    #print lucky_search(index, ranks, 'the')
    assert search.lucky_search(index, ranks, 'the') == nickel
    #print ordered_search(index, ranks, 'the')
    assert search.ordered_search(index, ranks, 'the') == [nickel, arsenic, hummus, indexurl]
    #print lucky_search(index, ranks, 'babaganoush')
    assert search.lucky_search(index, ranks, 'babaganoush') == None
    assert search.ordered_search(index, ranks, 'babaganoush') == None
    print "Finished tests."

test_engine()

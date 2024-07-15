import feedparser

rss_url = "http://rss.arxiv.org/rss/" + 'math.AG'
Feed = feedparser.parse(rss_url)
pointer = Feed.entries

print(pointer)

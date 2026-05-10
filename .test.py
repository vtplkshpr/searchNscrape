# pip install firecrawl-py
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-11c27285cec248dc83a20af5bcdf53c4")

# Scrape a website:
app.scrape('firecrawl.dev')
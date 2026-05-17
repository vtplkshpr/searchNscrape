from firecrawl import Firecrawl

from main import SearchNScrape

config = SearchNScrape._load_config()
firecrawl = Firecrawl(api_key=config.get("api_keys_for_searching.firecrawl"))

results = firecrawl.search(
    query="firecrawl",
    limit=3,
)
print(results)


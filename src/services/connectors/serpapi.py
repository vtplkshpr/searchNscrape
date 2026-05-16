import serpapi
import os
import json

from src.common.config import load_config
from src.common.logger import logger

config = load_config()
API_KEY = config.get("api_keys_for_searching.serpapi")
client = serpapi.Client(api_key=API_KEY)

class SerpApiSearch():
    def __init__(self):
        self.client = client

    def execute(self, engine="google", query=None, location=None, google_domain=None, hl=None, gl=None):
        try:
            results = self.client.search({
                "engine": engine,
                "q": query,
                "location": location,
                "google_domain": google_domain,
                "hl": hl,
                "gl": gl
            })
            logger.success("SerpApi search executed successfully.")
            return results
            #return results
        except Exception as e:
            logger.error(f"Error executing SerpApi search: {str(e)}")

# serpapi_search = SerpApiSearch()
# result = serpapi_search.execute(query="coffee")
# print(result)
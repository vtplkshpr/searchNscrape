#from src.core.framework import BaseSkill
import os
import json

from src.services.connectors.serpapi import SerpApiSearch
#class SearchNScrape(BaseSkill):
class SearchNScrape():
    @staticmethod
    def load_config(config_path=None):
        if config_path is None:
            # Set default config path based on module location
            base_dir = os.path.dirname(__file__)
            config_path = os.path.join(base_dir, "config.json")
        
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                return json.load(f)
        return {}

    def _load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return json.load(f)
        return {}

    @property
    def skill_name(self) -> str:
        config = self._load_config
        name = config.get("name")
        return name
    
    @property
    def config_path(self) -> str:
        # Override to set config path based on module location
        base_dir = os.path.dirname(__file__)
        return os.path.join(base_dir, "config.json")

    def execute(self, *args, **kwargs):
        query = input("Enter your search query: ")
        
        serpapi_search = SerpApiSearch()
        results = serpapi_search.execute(query=query)
        web_results = results.get("organic_results", [])
        print(f"Page: {results.get('pagination').get('current')}")
        for result in web_results:
            print(f"Position: {result.get('position')}")
            print(f"Title: {result.get('title')}")
            print(f"Link: {result.get('link')}")
            print(f"Snippet: {result.get('snippet')}")
            print("-" * 50)

def main():
    search_n_scrape = SearchNScrape()
    search_n_scrape.execute()

if __name__ == "__main__":
    main()
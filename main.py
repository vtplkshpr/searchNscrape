#from src.core.framework import BaseSkill
import os
import json
import pandas as pd
from datetime import datetime

from src.common.logger import logger
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
        file_path = input("Enter the file path to save results (e.g., search_results.parquet): ")
        file_type = input("Enter the file type to save results (e.g., parquet, csv): ").lower()
        base_dir = os.path.dirname(__file__)
        if file_path:
            file_path = os.path.abspath(file_path)
        else:
            file_path = os.path.abspath(os.path.join(base_dir, "storages", file_type, f"search_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{file_type}"))
        serpapi_search = SerpApiSearch()
        results = serpapi_search.execute(query=query)
        web_results = results.get("organic_results", [])
        pagination = results.get("pagination", {}).get("current", 1)
        print(f"Page: {pagination}")
        df_list = []
        for result in web_results:
            df = pd.DataFrame([{
                "pagination": pagination,
                "position": result.get("position"),
                "title": result.get("title"),
                "link": result.get("link"),
                "snippet": result.get("snippet")
            }])
            df_list.append(df)
            print(f"Position: {result.get('position')}")
            print(f"Title: {result.get('title')}")
            print(f"Link: {result.get('link')}")
            print(f"Snippet: {result.get('snippet')}")
            print("-" * 50)

        if df_list:
            final_df = pd.concat(df_list, ignore_index=True)
            if file_type == "parquet":
                final_df.to_parquet(file_path, index=False)
            elif file_type == "csv":
                final_df.to_csv(file_path, index=False)
            logger.success(f"Search results saved to {file_path}")
            print(f"Results saved to {file_path}")
        else:
            logger.error("No results found to save.")

def main():
    search_n_scrape = SearchNScrape()
    search_n_scrape.execute()

if __name__ == "__main__":
    main()
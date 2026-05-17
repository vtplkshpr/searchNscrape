from src.services.connectors.serpapi_connector import SerpApiSearch
from src.common.logger import logger

class ConnectorsController:
    def __init__(self):
        self.serpapi_connector = SerpApiSearch()

    def dispatch(self, query, *args, **kwargs):
        serpapi_result = self.serpapi_connector.execute(query=query, *args, **kwargs)
        return serpapi_result
import os

from main import SearchNScrape

config = SearchNScrape._load_config()
SUCCESS_LOG = config.get("logging.success_log")
ERROR_LOG = config.get("logging.error_log")


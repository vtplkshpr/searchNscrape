import json
import logging
import os

from src.common.config import config_path, load_config

config = load_config()
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SUCCESS_LOG = os.path.abspath(os.path.join(base_dir, "logs", config.get("logging").get("success_log")))
ERROR_LOG = os.path.abspath(os.path.join(base_dir, "logs", config.get("logging").get("error_log")))   

class Logger:
    def __init__(self):
        self.success_logger = self._setup_logger(
            'success_logger', 
            SUCCESS_LOG, 
            logging.INFO
        )
        self.error_logger = self._setup_logger(
            'error_logger', 
            ERROR_LOG, 
            logging.ERROR
        )

    def _setup_logger(self, name, log_file, level):
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler(log_file, encoding='utf-8')
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def success(self, message):
        self.success_logger.info(message)

    def error(self, message):
        self.error_logger.error(message, exc_info=True)

# Khởi tạo instance dùng chung
logger = Logger()
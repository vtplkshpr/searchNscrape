import json
import os

def config_path():
    # Set default config path based on module location
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(base_dir, "config.json")

def load_config(config_path=None):
    if config_path is None:
        # Set default config path based on module location
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        config_path = os.path.join(base_dir, "config.json")
    
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

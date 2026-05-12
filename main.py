#from src.core.framework import BaseSkill
import os
import json

#class SearchNScrape(BaseSkill):
class SearchNScrape():
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
        config = self._load_config()

        print("--- {self.skill_name()} Running ---")
        print(f"Config: {self.config_path}")

        # Demo logic
        name = config.get("name", "World")
        print(f"Hello, {name}!")
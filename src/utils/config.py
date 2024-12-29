import yaml
from pathlib import Path

def load_config(config_path: str = 'config/default.yaml') -> dict:
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
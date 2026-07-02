import json
import os

path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(path, 'r') as f:
    config = json.load(f)
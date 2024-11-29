import os
import sys
import json
json_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(json_file) as f:
    data = json.load(f)

print(data)
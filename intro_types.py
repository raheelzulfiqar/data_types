"""
Let's learn about Python types!
"""

import json

with open("raw_data/data.json", "r") as json_file:
    text = json_file.read()
    data = json.loads(text)


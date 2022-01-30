# jtest.py

import json

with open("people.json", 'r') as open_file:
    json_object = json.load(open_file)
    
print(json_object["person"][1]["id"])
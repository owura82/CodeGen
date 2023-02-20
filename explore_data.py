import sys
import json

data = open('dataset.jsonl', 'r').readlines()


types = {}
for entry in data:
    temp = json.loads(entry)
    print(temp.keys())
    break
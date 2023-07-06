import json

with open('movies.json', 'r') as file:
    data = json.load(file)

print(data)

import requests

r=requests.get("https://traveller.talrop.works/api/v1/places/")
print(r.json())
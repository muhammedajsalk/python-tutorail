import requests

params={
    "q":"tok"
}
r=requests.get("https://traveller.talrop.works/api/v1/places",params=params)
print(r.json())
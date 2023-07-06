import requests

data={
    "username":"sobir009@example.com",
    "password":"qwerty123"
}
r=requests.post("https://traveller.talrop.works/api/v1/auth/token/",data=data)

login_info = r.json()

access=login_info["access"]

#print(access)

headers={
    "Authorization" : f"Bearer {access}"
}

protected_requst=requests.get("https://traveller.talrop.works/api/v1/places/protected/30/",headers=headers)

print(protected_requst.text)
import requests

data={
    "username":"sobir009@example.com",
    "password":"qwerty123"
}
r=requests.post("https://traveller.talrop.works/api/v1/auth/token/",data=data)

login_info = r.json()

access=login_info["access"]

print(access)

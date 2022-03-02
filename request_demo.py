import requests

# r = requests.get("https://xkcd.com/353/")
# print(r.ok)
# print(r.status_code)
# print(r.headers)

# download and save image
# res = requests.get("https://imgs.xkcd.com/comics/python.png") 
# with open("./pngs/comic.png", 'wb') as f:
#     f.write(res.content)

# payload = {'page': 2, 'count': 25}
# res = requests.get("https://httpbin.org/get", params=payload)
# print(res.url)

# payload = {"username": "musleh", "password": "mypasswd"}
# response = requests.post("https://httpbin.org/post", data=payload)
# r_dict = response.json()
# print(r_dict['form'])

# authentication
response = requests.get("https://httpbin.org/basic-auth/musleh/mypasswd", auth=("musleh", "mypasswd"))
print(response.text)

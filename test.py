import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "/helloworld/tim")
response = requests.put(BASE + "video/1", { "likes": 10, "name": "Tim", "views": 100000 })
print(response.json())
response = requests.get(BASE + "video/1")
print(response.json())

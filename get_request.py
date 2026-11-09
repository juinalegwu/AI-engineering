import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json())

data = response.json()
print(data["url"])


student = {
    "name": "Juliet",
    "country": "Nigeria",
    "course": "AI Engineering"
}
print(student["course"])

import json

student = {
    "name": "Juliet",
    "course": "AI Engineering",

}
result = json.dumps(student)
print(result)

 
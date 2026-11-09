import json

student = {
    "name": "Juliet", 
    "course": "AI Engineering",
    "country": "Nigeria"
}
json_data = json.dumps(student)
python_data = json.loads(json_data)
print(python_data["name"])
print(python_data["course"])
print(python_data["country"])
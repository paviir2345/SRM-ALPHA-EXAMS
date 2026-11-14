import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

person_json = json.dumps(person)
print(person_json)

person_json2 = json.dumps(
    person,
    indent=4,
    separators=("; ", "= "),
    sort_keys=True
)

print(person_json2)
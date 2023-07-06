import json

python_obj={
    "name":"David",
    "class":1,
    "age":6
}


json_obj = json.dumps(python_obj)

print(json_obj)
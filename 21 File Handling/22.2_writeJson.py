import json

employee = {
    "name": "Ram",
    "age": 18,
    "grade": "A",
    "job": "cook"
}

file_path = "fileStuffs/output2.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4) # indent gives indentation by 4 spaces here to o/p file
    print(f"json file '{file_path}' was created")
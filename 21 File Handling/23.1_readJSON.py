import json

file_path = "fileStuffs/output2.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content['name']) # we can access the key values as well
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You do not have permission to read that file!")
except Exception:
    print("Something went wrong!")
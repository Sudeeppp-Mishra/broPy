file_path = "fileStuffs/output1.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError: # this exception is thrown when we don't have permission to read
    print("You do not have permission to read that file!")
except Exception:
    print("Something went wrong!")
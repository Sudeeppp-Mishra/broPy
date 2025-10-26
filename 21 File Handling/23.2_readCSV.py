import csv

file_path = "fileStuffs/output3.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # it gives memory address 
        print(content)
        
        for line in content:
            print(line)
            # print(line[0]) # This gives u first column -> here Name
            
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You do not have permission to read that file!")
except Exception:
    print("Something went wrong!")
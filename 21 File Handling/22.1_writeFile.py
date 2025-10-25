employees = ["Eugene", "Squidward", "Ram", "Shyam"]

file_path = "fileStuffs/output1.txt"

with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee+"\n")
    print(f"txt file '{file_path} is created!")
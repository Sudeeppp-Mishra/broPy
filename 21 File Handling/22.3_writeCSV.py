
import csv

employees = [["Name",  "Age", "Job"],
             ["Ram", 19, "Cook"],
             ["Krishna", 20, "Unemployed"],
             ["Ram", 30, "Doctor"]]

file_path = "fileStuffs/output3.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"CSV file '{file_path}' was created!")

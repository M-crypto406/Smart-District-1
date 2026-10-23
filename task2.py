import csv
import os
from datetime import datetime

os.makedirs("reports", exist_ok=True)

results = []
failed = []

try:
    with open("students.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                name = row["name"].strip()
                marks = float(row["marks"])

                if not name or marks < 0 or marks > 100:
                    raise ValueError("Invalid record")

                status = "Pass" if marks >= 40 else "Fail"

                student = {
                    "name": name,
                    "marks": marks,
                    "status": status
                }

                results.append(student)

                if status == "Fail":
                    failed.append(student)

            except (ValueError, KeyError, TypeError):
                print("Skipping invalid row:", row)

except FileNotFoundError:
    print("CSV file not found.")
    raise SystemExit

time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"reports/results_{time}.csv"

with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["name", "marks", "status"]
    )
    writer.writeheader()
    writer.writerows(results)

print("Valid students:", len(results))
print("Failed students:")

for student in failed:
    print(student["name"], student["marks"])

print("Report saved:", filename)
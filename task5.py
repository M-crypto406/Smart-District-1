employees = [
    {"id": 1, "name": "Ali", "salary": 50000, "experience": 3},
    {"id": 2, "name": "Sara", "salary": 60000, "experience": 4},
    {"id": 3, "name": "Ahmed", "salary": 60000, "experience": 6},
    {"id": 4, "name": "Zara", "salary": 45000, "experience": 5}
]

employees.sort(
    key=lambda e: (-e["salary"], -e["experience"], e["name"])
)

for rank, employee in enumerate(employees, start=1):
    print(rank, employee["name"], employee["salary"])

try:
    search_id = int(input("Enter employee ID: "))

    found = False

    for employee in employees:
        if employee["id"] == search_id:
            print("Employee found:", employee)
            found = True
            break

    if not found:
        print("Employee not found.")

except ValueError:
    print("Enter a valid ID.")
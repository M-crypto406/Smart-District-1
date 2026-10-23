import csv
import os
import logging
import asyncio
from datetime import datetime, timedelta
from functools import wraps

PASS_MARKS = int(os.getenv("PASS_MARKS", 40))

os.makedirs("reports", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/portal.log",
    level=logging.INFO
)


class PortalError(Exception):
    pass


class Student:
    def __init__(self, sid, name, department, marks, submitted):
        self.sid = sid
        self.name = name
        self.department = department
        self.marks = marks
        self.submitted = submitted

    @property
    def grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        elif self.marks >= PASS_MARKS:
            return "E"
        return "F"

    @property
    def status(self):
        if self.marks >= PASS_MARKS:
            return "Pass"
        return "Fail"


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Running %s", func.__name__)
        return func(*args, **kwargs)
    return wrapper


class AcademicPortal:
    def __init__(self):
        self.students = []

    @log_action
    def load_students(self):
        try:
            with open("students.csv", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        marks = float(row["marks"])

                        if not 0 <= marks <= 100:
                            raise ValueError("Invalid marks")

                        student = Student(
                            row["id"],
                            row["name"],
                            row["department"],
                            marks,
                            row["submitted"]
                        )
                        self.students.append(student)

                    except (ValueError, KeyError):
                        print("Skipping invalid row:", row)

        except FileNotFoundError:
            raise PortalError("students.csv not found")

    def show(self, students):
        for s in students:
            print(s.sid, s.name, s.department,
                  s.marks, s.grade, s.status)

    def failed(self):
        return [s for s in self.students if s.status == "Fail"]

    def late(self):
        result = []
        cutoff = datetime.now().date() - timedelta(days=7)

        for s in self.students:
            try:
                date = datetime.strptime(
                    s.submitted, "%Y-%m-%d"
                ).date()

                if date < cutoff:
                    result.append(s)

            except ValueError:
                logging.warning("Invalid date for %s", s.name)

        return result

    def summary(self):
        departments = {}

        for s in self.students:
            departments.setdefault(s.department, []).append(s)

        for name, students in departments.items():
            average = sum(s.marks for s in students) / len(students)
            print(name, "Count:", len(students),
                  "Average:", round(average, 2))

    @log_action
    def save_reports(self):
        time = datetime.now().strftime("%Y%m%d_%H%M%S")

        groups = {
            "results": self.students,
            "failed": self.failed(),
            "late": self.late()
        }

        for name, students in groups.items():
            filename = f"reports/{name}_{time}.csv"

            with open(filename, "w", newline="") as file:
                fields = [
                    "id", "name", "department",
                    "marks", "grade", "status", "submitted"
                ]
                writer = csv.writer(file)
                writer.writerow(fields)

                for s in students:
                    writer.writerow([
                        s.sid, s.name, s.department,
                        s.marks, s.grade, s.status, s.submitted
                    ])

            print("Saved:", filename)

    async def dashboard(self):
        await asyncio.sleep(0)

        print("Total students:", len(self.students))
        print("Failed students:", len(self.failed()))
        print("Late submissions:", len(self.late()))

        if self.students:
            average = sum(s.marks for s in self.students) / len(self.students)
            print("Average marks:", round(average, 2))


def main():
    portal = AcademicPortal()

    try:
        portal.load_students()
    except PortalError as error:
        logging.error("%s", error)
        print(error)
        return

    while True:
        print("\n1. All students")
        print("2. Failed students")
        print("3. Late submissions")
        print("4. Department summary")
        print("5. Save reports")
        print("6. Dashboard")
        print("0. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                portal.show(portal.students)
            elif choice == "2":
                portal.show(portal.failed())
            elif choice == "3":
                portal.show(portal.late())
            elif choice == "4":
                portal.summary()
            elif choice == "5":
                portal.save_reports()
            elif choice == "6":
                asyncio.run(portal.dashboard())
            elif choice == "0":
                break
            else:
                print("Invalid choice")

        except (OSError, ValueError, PortalError) as error:
            logging.exception("Operation failed")
            print("Error:", error)


if __name__ == "__main__":
    main()
import os
import json
from datetime import datetime, timedelta

folder = input("Enter project folder: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    raise SystemExit

files = []
cutoff = datetime.now() - timedelta(days=30)

for root, dirs, names in os.walk(folder):
    for name in names:
        path = os.path.join(root, name)

        try:
            size = os.path.getsize(path)
            modified = datetime.fromtimestamp(
                os.path.getmtime(path)
            )

            files.append({
                "name": path,
                "size": size,
                "modified": str(modified),
                "flagged": modified < cutoff
            })

        except OSError as error:
            print("Could not scan:", path, error)

report = {
    "folder": folder,
    "files": files
}

time = datetime.now().strftime("%Y%m%d_%H%M%S")

with open(f"audit_{time}.json", "w") as file:
    json.dump(report, file, indent=4)

print("Files scanned:", len(files))
print("Audit report created.")
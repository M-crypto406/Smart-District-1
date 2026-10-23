from collections import Counter

def read_errors(filename):
    with open(filename) as file:
        for line in file:
            if "ERROR:" in line:
                yield line.strip()

counts = Counter()

try:
    for line in read_errors("server.log"):
        error_type = line.split(":", 1)[1].strip()
        counts[error_type] += 1

        print(line)
        print("Running count:", dict(counts))

except FileNotFoundError:
    print("Log file not found.")

print("Final counts:", dict(counts))
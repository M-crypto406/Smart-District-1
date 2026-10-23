products = [
    {"name": "Laptop", "category": "Electronics", "price": 80000},
    {"name": "Mouse", "category": "Electronics", "price": 1200},
    {"name": "Phone", "category": "Electronics", "price": 50000},
    {"name": "Chair", "category": "Furniture", "price": 6000},
    {"name": "Desk", "category": "Furniture", "price": 12000}
]

categories = {}

for p in products:
    try:
        price = float(p["price"])

        if price < 0:
            continue

        category = p["category"]
        categories.setdefault(category, []).append({
            "name": p["name"],
            "price": price
        })

    except (ValueError, TypeError, KeyError):
        continue

summary = {}

for category, items in categories.items():
    items.sort(key=lambda p: p["price"], reverse=True)

    print("\n", category)

    for p in items[:5]:
        print(p["name"], p["price"])

    summary[category] = {
        "count": len(items),
        "average_price": sum(p["price"] for p in items) / len(items)
    }

print("\nSummary:", summary)
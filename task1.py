products = [
    {"name": "Laptop", "category": "Electronics", "price": "50000"},
    {"name": "Mouse", "category": "Electronics", "price": 1500},
    {"name": "Chair", "category": "Furniture", "price": "6000"},
    {"name": "Laptop", "category": "Electronics", "price": "50000"},
    {"name": "Phone", "category": "Electronics", "price": "abc"},
    {"name": "Table", "category": "Furniture", "price": None}
]

cleaned = []
seen = set()

for p in products:
    try:
        name = p["name"].strip()
        category = p["category"].strip()
        price = float(p["price"])

        if not name or not category or price < 0:
            continue

        key = (name.lower(), category.lower(), price)

        if key not in seen:
            seen.add(key)
            cleaned.append({
                "name": name,
                "category": category,
                "price": price
            })

    except (ValueError, TypeError, KeyError):
        print("Invalid product:", p.get("name", "Unknown"))

categories = {}

for p in cleaned:
    categories.setdefault(p["category"], []).append(p)

for category, items in categories.items():
    print("\nCategory:", category)

    items.sort(key=lambda p: p["price"])

    for p in items:
        print(p["name"], "-", p["price"])

    print("Total products:", len(items))
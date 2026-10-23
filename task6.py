from functools import reduce

orders = [
    {"id": 1, "amount": 5000, "category": "electronics"},
    {"id": 2, "amount": 800, "category": "clothing"},
    {"id": 3, "amount": 12000, "category": "electronics"},
    {"id": 4, "amount": 2500, "category": "clothing"}
]

valid = list(filter(lambda o: o["amount"] >= 1000, orders))

def discount(order):
    rate = 0.15 if order["category"] == "electronics" else 0.10

    return {
        **order,
        "final_price": order["amount"] * (1 - rate)
    }

processed = list(map(discount, valid))

total = reduce(
    lambda amount, order: amount + order["final_price"],
    processed,
    0
)

for order in processed:
    print(order)

print("Total revenue:", round(total, 2))
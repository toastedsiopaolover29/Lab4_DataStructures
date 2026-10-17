# Student-specific inputs
LAST_NAME = "Bautista"
STUDENT_ID = "TUPM-26-3506"
FAVORITE_ARTIST = "SABRINA CARPENTER"

# Get SEED_NUM
SEED_NUM = int(STUDENT_ID[-1])

artist_chars = FAVORITE_ARTIST.replace(" ", "")


def generate_value(position):
    letter = artist_chars[position - 1]
    alphabetical_value = ord(letter.upper()) - 64
    return alphabetical_value + (position * SEED_NUM)


customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

products = [
    "Notebook",
    "Pen",
    "USB",
    "Headphones",
    "Calculator"
]

quantities = [
    (generate_value(pos) % 5) + 1
    for pos in range(1, 6)
]

prices = [50, 20, 150, 500, 250]

transactions = []

for customer, product, qty, price in zip(
    customers,
    products,
    quantities,
    prices
):
    transactions.append({
        "customer": customer,
        "product": product,
        "quantity": qty,
        "price": price,
        "total": qty * price
    })

# Repeated purchase
transactions.append(transactions[2])

# ------
# PREPARE DATA FOR REPORTING

distinct = []
for transaction in transactions:
    if transaction not in distinct:
        distinct.append(transaction)

organized_transaction_data = {}
product_summary = {}
customer_summary = {}

for transaction in distinct:
    product = transaction["product"]
    customer = transaction["customer"]
    total = transaction["total"]

    organized_transaction_data.setdefault(product, []).append(transaction)
    product_summary[product] = product_summary.get(product, 0) + total
    customer_summary[customer] = customer_summary.get(customer, 0) + total

transaction_values = [
    transaction["total"]
    for transaction in distinct
]

ordered_results = sorted(transaction_values)

overall_summary = {
    "Total Sales": sum(transaction_values),
    "Highest Transaction": max(transaction_values),
    "Average Transaction": round(
        sum(transaction_values) / len(transaction_values),
        2
    )
}

repeated_transactions = [transactions[-1]]

# ------
# ASSESSMENT DATA


print("=" * 50)
print("ASSESSMENT DATA")
print("=" * 50)

print("\n1. Generated Transaction Records")
print(transactions)

print("\n2. Organized Transaction Data")
print(product_summary)

print("\n3. Distinct Transactions")
print(f"Unique Transactions: {len(distinct)}")

print("\n4. Transaction Values")
print(transaction_values)

print("\n5. Customer Summaries")
for customer, total in customer_summary.items():
    print(customer, ":", total)

print("\n6. Product Summaries")
print(product_summary)

print("\n7. Ordered Results")
print(ordered_results)

print("\n8. Overall Transaction Summary")
print(overall_summary)

# ------
# FINAL OUTPUT

print("\n" + "=" * 50)
print("FINAL OUTPUT")
print("=" * 50)

print("\nFinal Consolidated Transaction Report")

for product, total in product_summary.items():
    print(f"{product}: {total}")

print("\nRepeated Transaction:")
for item in repeated_transactions:
    print(
        f"{item['customer']} - "
        f"{item['product']} - "
        f"{item['total']}"
    )

print(f"\nTotal Sales = {overall_summary['Total Sales']}")
print(
    f"Highest Transaction = "
    f"{overall_summary['Highest Transaction']}"
)
print(
    f"Average Transaction = "
    f"{overall_summary['Average Transaction']}"
)

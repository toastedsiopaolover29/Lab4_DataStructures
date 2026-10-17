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

print("GENERATED TRANSACTION DATA")
for transaction in transactions:
    print(transaction)

# Organize by customer
customer_summary = {}

for transaction in transactions[:5]:
    customer_summary[transaction["customer"]] = transaction["total"]

# Organize by product
product_summary = {}

for transaction in transactions[:5]:
    product_summary[transaction["product"]] = transaction["total"]

print("\nCUSTOMER SUMMARY")
for customer, total in customer_summary.items():
    print(customer, ":", total)

print("\nPRODUCT SUMMARY")
for product, total in product_summary.items():
    print(product, ":", total)

# Distinct transactions
distinct = set()

for transaction in transactions:
    distinct.add(
        (
            transaction["customer"],
            transaction["product"]
        )
    )

print("\nDISTINCT TRANSACTIONS")
print(len(distinct))

transaction_values = [
    t["total"] for t in transactions[:5]
]

print("\nTRANSACTION VALUES")
print(transaction_values)

print("\nORDERED RESULTS")
print(sorted(transaction_values))

total_sales = sum(transaction_values)
average_sale = total_sales / len(transaction_values)

print("\nOVERALL TRANSACTION SUMMARY")
print("Total Sales:", total_sales)
print("Highest Transaction:", max(transaction_values))
print("Average Transaction:", round(average_sale, 2))

print("\nFINAL CONSOLIDATED TRANSACTION REPORT")
for product, total in product_summary.items():
    print(product, ":", total)

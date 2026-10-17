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


# Generate test sources
sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]

# Categories
categories = ["Temperature", "Voltage", "Current", "Speed", "Temperature"]

# Generate values using SEED_NUM and artist character positions
values = [generate_value(pos) for pos in range(1, 6)]

# Create records
records = [
    {"source": sources[i], "category": categories[i], "value": values[i]}
    for i in range(5)
]

# Add repeated records
records.append(records[2])
records.append(records[1])

# Organize by category
organized = {}

for record in records:
    organized.setdefault(record["category"], []).append(record["value"])

# Distinct values
distinct_values = set()

for record in records:
    distinct_values.add(record["value"])

# Category averages
category_summaries = {}

for category, vals in organized.items():
    category_summaries[category] = round(
        sum(vals) / len(vals),
        2
    )

# Ordered values
ordered = sorted([r["value"] for r in records])

# Processed results
processed_results = {
    "highest": max(ordered),
    "lowest": min(ordered),
    "range": max(ordered) - min(ordered)
}

# ------
# ASSESSMENT DATA

print("=" * 50)
print("ASSESSMENT DATA")
print("=" * 50)

print("\n1. Generated Test Data")
print(records)

print("\n2. Organized Test Data")
print(organized)

print("\n3. Distinct Data")
print(distinct_values)

print("\n4. Numeric/Categorical Summaries")
print(category_summaries)

print("\n5. Processed Results")
print(processed_results)

print("\n6. Ordered Results")
print(ordered)

# ------
# FINAL OUTPUT

print("\n" + "=" * 50)
print("FINAL OUTPUT")
print("=" * 50)

print("\nFinal Organized and Summarized Test Dataset")

for category, vals in organized.items():
    print(f"{category}: {vals}")

print(f"\nHighest = {processed_results['highest']}")
print(f"Lowest = {processed_results['lowest']}")
print(f"Range = {processed_results['range']}")
print(f"Distinct Values = {len(distinct_values)}")

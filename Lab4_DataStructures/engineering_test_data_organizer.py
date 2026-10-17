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

print("GENERATED TEST DATA")
for record in records:
    print(record)

# Organize by category
organized = {}

for record in records:
    organized.setdefault(record["category"], []).append(record["value"])

print("\nORGANIZED TEST DATA")
for category, vals in organized.items():
    print(category, ":", vals)

# Distinct values
distinct_values = set()
for record in records:
    distinct_values.add(record["value"])

print("\nDISTINCT VALUES")
print(distinct_values)

# Category averages
print("\nCATEGORY SUMMARIES")
for category, vals in organized.items():
    avg = sum(vals) / len(vals)
    print(f"{category}: {avg:.2f}")

# Ordered values
ordered = sorted([r["value"] for r in records])

print("\nORDERED RESULTS")
print(ordered)

print("\nFINAL SUMMARY")
print("Highest:", max(ordered))
print("Lowest:", min(ordered))
print("Range:", max(ordered) - min(ordered))

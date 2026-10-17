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


subjects = (
    "Programming",
    "Mathematics",
    "Electronics",
    "Physics",
    "English"
)

students = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

scores = [
    80 + SEED_NUM + 0,
    80 + SEED_NUM + 3,
    80 + SEED_NUM + 6,
    80 + SEED_NUM + 9,
    80 + SEED_NUM + 12
]

records = []

for student, subject, score in zip(students, subjects, scores):
    records.append({
        "student": student,
        "subject": subject,
        "score": score
    })

# Repeated record
records.append(records[2])

# Incomplete record
records.append({
    "student": students[4],
    "subject": "English",
    "score": None
})

print("GENERATED PERFORMANCE RECORDS")
for record in records:
    print(record)

# Separate valid records
valid_records = [r for r in records if r["score"] is not None]

# Detect duplicates
seen = set()
duplicates = []

for record in valid_records:
    key = (record["student"], record["subject"])
    if key in seen:
        duplicates.append(record)
    else:
        seen.add(key)

print("\nREPEATED RECORDS")
for item in duplicates:
    print(item)

# Missing scores
print("\nINCOMPLETE RECORDS")
for item in records:
    if item["score"] is None:
        print(item)

# Categorize performance


def performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 85:
        return "Very Good"
    else:
        return "Good"


print("\nPERFORMANCE CATEGORY")
for record in valid_records[:5]:
    print(
        record["subject"],
        "-",
        performance(record["score"])
    )

# Subject summary
subject_data = {}

for record in valid_records[:5]:
    subject_data[record["subject"]] = record["score"]

print("\nSTUDENT SUMMARY")
average = sum(subject_data.values()) / len(subject_data)

print("Average:", round(average, 2))
print("Highest:", max(subject_data.values()))
print("Lowest:", min(subject_data.values()))

print("\nORDERED RESULTS")
print(sorted(subject_data.values()))

print("\nFINAL STUDENT PERFORMANCE REPORT")
for subject, score in subject_data.items():
    print(subject, ":", score)

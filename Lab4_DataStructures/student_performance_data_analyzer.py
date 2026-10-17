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


def performance(score):
    if score >= 90:
        return "Excellent"
    if score >= 80:
        return "Good"
    if score >= 70:
        return "Satisfactory"
    return "Needs Improvement"


subjects = (
    "Programming",
    "Mathematics",
    "Electronics",
    "Physics",
    "English"
)

students = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

scores = [
    min(100, 70 + generate_value(pos))
    for pos in range(1, 6)
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

# ----
# PREPARE DATA FOR REPORTING

# Incomplete records
incomplete_records = [
    record for record in records
    if record["score"] is None
]

valid_records = [
    record for record in records
    if record["score"] is not None
]

duplicates = [
    record for index, record in enumerate(records)
    if record in records[:index]
]

# Performance categories
performance_categories = {}

for record in valid_records[:5]:
    performance_categories[record["subject"]] = performance(
        record["score"]
    )

# Subject summary
subject_data = {}

for record in valid_records[:5]:
    subject_data[record["subject"]] = record["score"]

average = round(
    sum(subject_data.values()) / len(subject_data),
    2
)

student_summary = {
    "Average": average,
    "Highest": max(subject_data.values()),
    "Lowest": min(subject_data.values())
}

ordered_results = sorted(subject_data.values())

# -----
# ASSESSMENT DATA

print("=" * 50)
print("ASSESSMENT DATA")
print("=" * 50)

print("\n1. Generated Performance Records")
print(records)

print("\n2. Organized Performance Data")
print(subject_data)

print("\n3. Repeated/Incomplete Records")

print("\nRepeated Records:")
print(duplicates)

print("\nIncomplete Records:")
print(incomplete_records)

print("\n4. Performance Categories")
print(performance_categories)

print("\n5. Student and Subject Summaries")
print(student_summary)

print("\n6. Ordered Results")
print(ordered_results)

# -----
# FINAL OUTPUT

print("\n" + "=" * 50)
print("FINAL OUTPUT")
print("=" * 50)

print("\nFinal Student Performance Report")

for subject, score in subject_data.items():
    print(f"{subject}: {score}")

print(f"\nAverage = {student_summary['Average']}")
print(f"Highest = {student_summary['Highest']}")
print(f"Lowest = {student_summary['Lowest']}")

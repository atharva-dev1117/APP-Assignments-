import csv
import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Course Information System"
)

# Accept filename using argparse
parser.add_argument(
    "filename",
    help="CSV file containing course details"
)

args = parser.parse_args()

try:
    # Read course details from CSV file
    with open(args.filename, "r") as file:
        reader = csv.DictReader(file)
        courses = list(reader)

    # Display all course records
    print("\nCourse Records:")

    for course in courses:
        print(course)

    # Search using Course ID
    course_id = input("\nEnter Course ID to search: ")

    found = False

    for course in courses:
        if course["Course ID"] == course_id:
            print("\nCourse Found:")
            print(course)
            found = True
            break

    if not found:
        print("Course not found.")

except FileNotFoundError:
    print("File not found.")

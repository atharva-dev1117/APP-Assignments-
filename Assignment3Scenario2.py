import csv
import argparse

# Function to display all course records
def display_courses(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n----- Course Records -----")
        for row in reader:
            print("Course ID     :", row[0])
            print("Course Name   :", row[1])
            print("Instructor    :", row[2])
            print("Credits       :", row[3])
            print("Department    :", row[4])
            print("-" * 30)


# Function to search course by Course ID
def search_course(filename):
    course_id = input("Enter Course ID: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == course_id:
                print("\nCourse Found")
                print("Course ID     :", row[0])
                print("Course Name   :", row[1])
                print("Instructor    :", row[2])
                print("Credits       :", row[3])
                print("Department    :", row[4])
                found = True
                break

    if not found:
        print("Course Record Not Found.")


# Command-line argument using argparse
parser = argparse.ArgumentParser(
    description="Course Information System"
)

parser.add_argument(
    "filename",
    help="CSV file containing course records"
)

args = parser.parse_args()

filename = args.filename


# Main menu
while True:
    print("\n1. Display All Courses")
    print("2. Search Course")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_courses(filename)

    elif choice == "2":
        search_course(filename)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice")

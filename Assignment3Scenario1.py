import csv
import sys

# Function to display all grocery items
def display_items(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n----- Grocery Inventory -----")
        for row in reader:
            print("Item ID       :", row[0])
            print("Item Name     :", row[1])
            print("Quantity      :", row[2])
            print("Price         :", row[3])
            print("Category      :", row[4])
            print("-" * 30)


# Function to search grocery item by Item ID
def search_item(filename):
    item_id = input("Enter Item ID: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == item_id:
                print("\nItem Found")
                print("Item ID       :", row[0])
                print("Item Name     :", row[1])
                print("Quantity      :", row[2])
                print("Price         :", row[3])
                print("Category      :", row[4])
                found = True
                break

    if not found:
        print("Item Record Not Found.")


# Check command-line argument
if len(sys.argv) < 2:
    print("Please provide the CSV filename.")
    print("Example: python grocery.py grocery.csv")
    sys.exit()

filename = sys.argv[1]

while True:
    print("\n1. Display All Grocery Items")
    print("2. Search Grocery Item")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_items(filename)

    elif choice == "2":
        search_item(filename)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice")

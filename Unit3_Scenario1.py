import csv
import sys

# Check command-line argument
if len(sys.argv) != 2:
    print("Usage: python grocery.py <filename>")
    sys.exit()

filename = sys.argv[1]

try:
    # Read grocery records from CSV file
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    # Display all grocery items
    print("\nGrocery Inventory:")
    for item in records:
        print(item)

    # Search using Item ID
    item_id = input("\nEnter Item ID to search: ")

    found = False

    for item in records:
        if item["Item ID"] == item_id:
            print("\nItem Found:")
            print(item)
            found = True
            break

    if not found:
        print("Item not found.")

except FileNotFoundError:
    print("File not found.")

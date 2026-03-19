# Ex6.py - List traversal and element addition
# Initialize student names list
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Step 1: Iterate through the list and print names with last name "Evans"
print("Initial list with last name Evans:")
for name in studentNames:
    print(f"{name} Evans")

# Step 2: Get new name from user and add to list
new_name = input("\nEnter a new name to add to the list: ").strip()

# Step 3: Reprint the updated list
if new_name:
    studentNames.append(new_name)
    print("\nUpdated list with last name Evans:")
    for name in studentNames:
        print(f"{name} Evans")
else:
    print("Error: Name cannot be empty!")

# Start with an empty inventory list
inventory = []

# Function to add an item to the inventory
def add_item(item):
    inventory.append(item)

# Recursive function to count items
def count_items(items):
    # Base case: list is empty
    if not items:
        return 0
    # Recursive step
    return 1 + count_items(items[1:])

def main():
    # Add items using add_item()
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    # Lambda function to display items
    show_item = lambda item: print(f"Item in Stock: {item}")

    # Display every item in inventory
    for item in inventory:
        show_item(item)

    # Count total items using recursive function
    total = count_items(inventory)
    print(f"\nTotal items in inventory: {total}")

# Run the program
main()
# Bill management system

# Initialize an empty dictionary to store items and their prices
items = {}

# Function to add items and their prices to the dictionary
def add_item():
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the quantity: "))
    items[item_name] = {
        'price': item_price,
        'quantity': item_quantity
    }

# Function to calculate the total bill
def calculate_total():
    total = 0
    for item_name, item_info in items.items():
        item_price = item_info['price']
        item_quantity = item_info['quantity']
        total += item_price * item_quantity
    return total

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add an item")
    print("2. Calculate the total bill")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        total_bill = calculate_total()
        print(f"Total Bill: ${total_bill:.2f}")
    elif choice == '3':
        print("Thank you. Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
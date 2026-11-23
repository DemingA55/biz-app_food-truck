import csv

inventory = {}
sales = []


# Loads food items from the inventory CSV file
def load_inventory():
    """Reads inventory.csv and loads the data into the inventory dictionary"""

    with open("inventory.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) == 3:
                item = row[0]
                price = float(row[1])
                quantity = int(row[2])

                inventory[item] = {
                    "price": price,
                    "quantity": quantity
                }


# Loads previous sales transactions from the CSV file
def load_sales():
    """Reads sales.csv and loads previous transactions into the sales list"""

    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) == 4:
                item = row[0]
                quantity = int(row[1])
                price = float(row[2])
                total = float(row[3])

                sale = {
                    "item": item,
                    "quantity": quantity,
                    "price": price,
                    "total": total
                }

                sales.append(sale)


# Saves sales transactions to the CSV file
def save_sales():
    """Writes the sales list to sales.csv"""

    with open("sales.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(["item", "quantity", "price", "total"])

        for sale in sales:
            writer.writerow([
                sale["item"],
                sale["quantity"],
                sale["price"],
                sale["total"]
            ])


# Records a customer sale and updates inventory
def record_sale():
    """Records a sale and reduces the available inventory"""

    # Ask which food item was sold
    while True:
        item = input("Enter food item name (or B to cancel): ").strip()

        if item.lower() == "b":
            print("Sale canceled.")
            return

        existing_item = ""

        for name in inventory:
            if name.lower() == item.lower():
                existing_item = name
                break

        if existing_item != "":
            break

        else:
            print("Item not found. Please try again.")

    # Ask how many items were sold
    while True:
        quantity_input = input("Enter quantity sold (or B to cancel): ").strip()

        if quantity_input.lower() == "b":
            print("Sale canceled.")
            return

        elif quantity_input.isdigit():
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity must be greater than zero.")

            elif quantity > inventory[existing_item]["quantity"]:
                print("Not enough inventory available. Please try again.")

            else:
                break

        else:
            print("Invalid quantity. Please try again.")

    # Calculate the sale
    price = inventory[existing_item]["price"]
    total = price * quantity

    # Create a transaction dictionary
    sale = {
        "item": existing_item,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    # Add the transaction to the sales list
    sales.append(sale)

    # Reduce the available inventory
    inventory[existing_item]["quantity"] -= quantity

    # Display the sale information
    print("\n=== Sale Recorded ===")
    print(f"Item: {existing_item}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")
    print(f"Remaining inventory: {inventory[existing_item]['quantity']}\n")


# Saves the current inventory to the CSV file
def save_inventory():
    """Writes the inventory dictionary to inventory.csv"""

    with open("inventory.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(["item", "price", "quantity"])

        for item, details in inventory.items():
            writer.writerow([item, details["price"], details["quantity"]])


# Displays all food items and their inventory details
def view_inventory():
    """Displays all food items and their inventory details"""

    print("\n=== Big Sky Bites Inventory ===\n")

    for item, details in inventory.items():
        print(f"{item}: ${details['price']:.2f}, Quantity: {details['quantity']}")

    input("\nPress 'Enter' to return to the main menu...")


# Allows the user to add or update food items
def update_inventory():
    """Allows the user to add or update food items"""

    item = input("Enter food item name (or B to go back): ").strip()

    if item.lower() == "b":
        return

    if item == "":
        print("Please enter a food item name.")
        return

    existing_item = ""

    for name in inventory:
        if name.lower() == item.lower():
            existing_item = name
            break

    if existing_item != "":
        print(f"{existing_item} already exists in inventory.")

        print("1. Change Price")
        print("2. Change Quantity")

        choice = input("Enter 1 or 2: ")

        while choice != "1" and choice != "2":
            print("Invalid option. Please try again.")
            choice = input("Enter 1 or 2: ")

        if choice == "1":

            while True:
                new_price = input("Enter new price (or B to cancel): ").strip()

                if new_price.lower() == "b":
                    print("Update canceled.")
                    return

                elif new_price.replace(".", "", 1).isdigit():
                    inventory[existing_item]["price"] = float(new_price)
                    print("Price updated successfully!")
                    break

                else:
                    print("Invalid price. Please try again.")

        elif choice == "2":

            while True:
                new_quantity = input("Enter new quantity (or B to cancel): ").strip()

                if new_quantity.lower() == "b":
                    print("Update canceled.")
                    return

                elif new_quantity.isdigit():
                    inventory[existing_item]["quantity"] = int(new_quantity)
                    print("Quantity updated successfully!")
                    break

                else:
                    print("Invalid quantity. Please try again.")

    else:
        print(f"{item} is not currently in inventory.")

        # Get the price
        while True:
            new_price = input("Enter price (or B to cancel): ").strip()

            if new_price.lower() == "b":
                print("Item addition canceled.")
                return

            elif new_price.replace(".", "", 1).isdigit():
                break

            else:
                print("Invalid price. Please try again.")

        # Get the quantity
        while True:
            new_quantity = input("Enter quantity (or B to cancel): ").strip()

            if new_quantity.lower() == "b":
                print("Item addition canceled.")
                return

            elif new_quantity.isdigit():
                break

            else:
                print("Invalid quantity. Please try again.")

        # Confirm the new item
        print(f"\nItem: {item}")
        print(f"Price: ${float(new_price):.2f}")
        print(f"Quantity: {new_quantity}")

        while True:
            confirm = input("Add this item? (Y/N): ").lower().strip()

            if confirm == "y":
                inventory[item] = {
                    "price": float(new_price),
                    "quantity": int(new_quantity)
                }

                print(f"{item} added successfully!")
                break

            elif confirm == "n" or confirm == "b":
                print("Item addition canceled.")
                break

            else:
                print("Invalid option. Please enter Y or N.")


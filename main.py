# main functions


# Code to run is below:
# cd C:\Users\asher\Desktop\Food_truck_app
# python main.py  
"""
Remember: For all future commits, you only need these three commands:

git add .
git commit -m "Describe your changes"
git push

"""                        

import csv



# Displays the food truck's main menu
def show_menu():
    """Shows the food truck's main menu"""
    print(" === Big Sky Bites === \n")
    print("1. View Menu and Inventory")
    print("2. Update Inventory")
    print("3. Record a Sale")
    print("4. View Sales Report")
    print("5. Run Sales Simulation")
    print("6. Generate Charts")
    print("7. Save and Exit")


inventory = {}



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


load_inventory()
while True:
    show_menu()
    print()
    user_input = input("Enter a number 1-7: ")

    if user_input == "7":
        save_inventory()
        print("Exiting program...\n")
        break

    elif user_input == "1":
        view_inventory()
    
    elif user_input == "2":
        update_inventory()
    
    elif user_input in ["3", "4", "5", "6"]:
        print("Coming soon!\n")
        
    else:
        print("Invalid option. Please enter a number 1-7.\n")



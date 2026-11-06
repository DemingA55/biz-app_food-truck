# main functions


# Code to run is below:
# cd C:\Users\asher\Desktop\Food_truck_app
# python main.py                          

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


inventory = {
    "Tacos": {"price": 3.50, "quantity": 30},
    "Burritos": {"price": 8.00, "quantity": 20},
    "Quesadillas": {"price": 6.50, "quantity": 25},
    "Salad": {"price": 7.00, "quantity": 15},
    "Cookie": {"price": 2.00, "quantity": 40}
}

# Displays all food items and their inventory details
def view_inventory():
    """Displays all food items and their inventory details"""
    while True:
        print("\n=== Big Sky Bites Inventory ===\n")

        for item, details in inventory.items():
            print(f"{item}: ${details['price']:.2f}, Quantity: {details['quantity']}")

        print("\n1. Update or Add Item")
        print("2. Back to Main Menu")

        choice = input("\nChoose 1 or 2: ")

        if choice == "1":
            print("Coming soon!\n")

        elif choice == "2":
            return

        else:
            print("Invalid option. Try again.")
        

while True:
    show_menu()
    print()
    user_input = input("Enter a number 1-7: ")

    if user_input == "7":
        print("Exiting program...\n")
        break
    elif user_input == "1":
        view_inventory()
        print()
    elif user_input in ["2", "3", "4", "5", "6"]:
        print("Coming soon!\n")
    else:
        print("Invalid option. Please enter a number 1-7.\n")

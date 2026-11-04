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


while True:
    show_menu()
    print()
    user_input = input("Enter a number 1-7: ")

    if user_input == "7":
        print("Exiting program...\n")
        break
    elif user_input in ["1", "2", "3", "4", "5", "6"]:
        print("Coming soon!\n")
    else:
        print("Invalid option. Please enter a number 1-7.\n")

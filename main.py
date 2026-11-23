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

import reports
import big_sky_bites
import simulation

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


big_sky_bites.load_inventory()
big_sky_bites.load_sales()
while True:
    show_menu()
    print()
    user_input = input("Enter a number 1-7: ")
    
    if user_input == "7":
        big_sky_bites.save_inventory()
        big_sky_bites.save_sales()
        print("Inventory and sales saved successfully!")
        print("Exiting program...\n")
        break

    elif user_input == "1":
        big_sky_bites.view_inventory()
    
    elif user_input == "2":
        big_sky_bites.update_inventory()

    elif user_input == "3":
        big_sky_bites.record_sale()
    
    elif user_input == "4":
        reports.view_sales_report(big_sky_bites.sales)
        input("\nPress Enter to return to the main menu...")

    elif user_input == "5":
        simulation.run_simulation()
        input("\nPress Enter to return to the main menu...")

    elif user_input == "6":
        reports.generate_charts(big_sky_bites.sales)
        
    else:
        print("Invalid option. Please enter a number 1-7.\n")


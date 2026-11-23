import matplotlib.pyplot as plt

# Groups sales transactions by food item
def group_sales_by_item(sales):
    """Calculates total quantities and revenue for each food item"""

    item_totals = {}

    for sale in sales:
        item = sale["item"]

        if item in item_totals:
            item_totals[item]["quantity"] += sale["quantity"]
            item_totals[item]["revenue"] += sale["total"]

        else:
            item_totals[item] = {
                "quantity": sale["quantity"],
                "revenue": sale["total"]
            }

    return item_totals



# Displays a summary of Big Sky Bites sales
def view_sales_report(sales):
    """Displays sales statistics and totals for each food item"""

    if len(sales) == 0:
        print("No sales transactions have been recorded yet.")
        return

    item_totals = group_sales_by_item(sales)

    total_revenue = 0
    total_items_sold = 0

    for sale in sales:
        total_revenue += sale["total"]
        total_items_sold += sale["quantity"]

    total_transactions = len(sales)
    average_sale = total_revenue / total_transactions

    # Find the best-selling item
    top_item = ""
    top_quantity = 0

    for item in item_totals:
        if item_totals[item]["quantity"] > top_quantity:
            top_item = item
            top_quantity = item_totals[item]["quantity"]

    # Display sales statistics
    print("\n=== Big Sky Bites Sales Report ===\n")

    print(f"Total transactions: {total_transactions}")
    print(f"Total items sold: {total_items_sold}")
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Average sale: ${average_sale:.2f}")
    print(f"Best-selling item: {top_item} ({top_quantity} sold)")

    # Display totals for individual food items
    print("\nSales by Item:")

    for item in item_totals:
        print(f"{item}: {item_totals[item]['quantity']} sold, "
              f"${item_totals[item]['revenue']:.2f} revenue")



# Generates charts from sales transactions
def generate_charts(sales):
    """Creates charts showing Big Sky Bites sales information"""

    if len(sales) == 0:
        print("No sales available. Record a sale first.")
        return

    # Group sales by food item
    item_totals = group_sales_by_item(sales)

    items = []
    quantities = []

    for item in item_totals:
        items.append(item)
        quantities.append(item_totals[item]["quantity"])

    # Create the bar chart
    plt.figure()
    plt.bar(items, quantities)

    plt.title("Units Sold by Menu Item")
    plt.xlabel("Menu Item")
    plt.ylabel("Units Sold")

    plt.savefig("units_sold_by_item.png")
    plt.show()


    # Prepare data for the line chart
    transaction_numbers = []
    sale_totals = []

    transaction_number = 1

    for sale in sales:
        transaction_numbers.append(transaction_number)
        sale_totals.append(sale["total"])

        transaction_number += 1

    # Create the line chart
    plt.figure()
    plt.plot(transaction_numbers, sale_totals, marker="o")

    plt.title("Revenue by Transaction")
    plt.xlabel("Transaction Number")
    plt.ylabel("Revenue ($)")

    plt.savefig("revenue_by_transaction.png")
    plt.show()


    print("Charts saved successfully!")

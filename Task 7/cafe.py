# List the items on the menu.
menu = ["americano", "cappuccino", "latte", "mocha", "tea"]

# Creating stock dictionary.
stock = {
    "americano": 30,
    "cappuccino": 40,
    "latte": 60,
    "mocha": 20,
    "tea": 70,
}

# Creating price dictionary.
price = {
    "americano": 3,
    "cappuccino": 4,
    "latte": 4,
    "mocha": 3.5,
    "tea": 3,
}
 
total_stock = 0.0
# Loop for items in the list.
for item in menu:
    # Get quantity for item.
    quantity = stock[item]
    # Get cost for item.
    cost = price[item]
    # Add value of item to total.
    total_stock += quantity * cost

print('The total stock worth is £ ', total_stock)
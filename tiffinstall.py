MENU = {
    "Idly": {
        "ingredients": {
            "water": 50,
            "batter": 100,
            "milk": 0,
            "oil": 0,
        },
        "cost": 5
    },
    "dosa": {
        "ingredients": {
            "water": 80,
            "batter": 150,
            "oil": 10,
            "milk": 0,
        },
        "cost": 10,
    },
    "appam": {
        "ingredients": {
            "water": 25,
            "milk": 25,
            "batter": 75,
            "oil": 0,
        },
        "cost": 12,
    }
}

profit = 0
resources = {
    "batter": 500,
    "water": 300,
    "oil": 50,
    "milk": 75,
}

def resource_is_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Out of stock for {item}.")
            return False
    return True

def bill(item_cost, quantity):
    return item_cost * quantity

def payment_done(bill_amount):
    global profit
    profit += bill_amount

def update_resources(choice, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice}.")

is_on = True

while is_on:
    choice = input("Choose dosa/Idly/appam (or type 'enough' to exit, 'report' to check resources): ")
    if choice == "enough":
        is_on = False
        total_bill=profit
        print("your total bill amount is:$ ",profit)
        print("Exiting...")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Batter: {resources['batter']}g")
        print(f"Oil: {resources['oil']}ml")
        print(f"Money: ${profit}")
    elif choice in MENU:
        quantity = int(input("Enter the quantity: "))
        tiffen = MENU[choice]
        if resource_is_sufficient(tiffen['ingredients']):
            cost = bill(tiffen["cost"], quantity)
            payment_done(cost)
            update_resources(choice, tiffen['ingredients'])
            '''print(f"Bill amount: ${cost}")'''
        else:
            print("Order cannot be processed due to insufficient resources.")
    else:
        print("Invalid choice. Please select from the menu options.")



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:   
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough 


def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quaters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennis?: ")) * 0.01
    return total

def is_transaction_successful(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    

def make_coffee(drink_name , order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


next_customer = False
while not next_customer:
    Choice = input("What would you like? (espresso/latte/cappuccino):")

    if Choice == "off":
        next_customer = True
    elif Choice == "report":
        print (f"water :{ resources('water')}ml")
        print (f"milk : {resources('milk')}ml")
        print (f"coffee : {resources('coffee')}g")
        print(f"money : ${profit}")
    else:
        drink = MENU[Choice]
        if resource_sufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(Choice , drink["ingredients"])
import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


COINS = {
    "quarters": 0.25, 
    "dimes": 0.10, 
    "nickles": 0.05, 
    "pennies": 0.01,
}


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def check_ingredients(coffee):
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if resources.get(ingredient, 0) < amount: # It avoid a key error
            print(f"Sorry! We do not have enough {ingredient}.")
            return False
    return True


def update_resources(coffee):
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        resources[ingredient] -= amount


def main():
    while True:
        print("-------------------------")
        print("1: Espresso, $1.5")
        print("2: Latte, $2.5")
        print("3: Capuccino, $3.0")
        print("-------------------------")
        user_input = input("Type the desired coffee number: ")
        
        if user_input == "off":
            print("Leaving...")
            break
        elif user_input == "report":
            print(f"{resources}")
            user_input = input("Type the desired coffee number: ")

        coffee = int(user_input)

        if coffee == 1:
            coffee = "espresso"
        elif coffee == 2:
            coffee = "latte"
        elif coffee == 3:
            coffee = "cappuccino"
        else:
            print("Type a valid answer!")
            continue

        if check_ingredients(coffee):
            print(f"We have enough resources to make your {coffee}.")
            
            update_resources(coffee)
            
            print("-------------------------")
            print("Please insert the coins:\n")
            num_quarters = int(input("How many quarters? "))
            num_dimes = int(input("How many dimes? "))
            num_nickels = int(input("How many nickles? "))
            num_pennies = int(input("How many pennies? "))


            total_value = (num_quarters * COINS["quarters"] + num_dimes * COINS["dimes"] +
            num_nickels * COINS["nickles"] + num_pennies * COINS["pennies"])

            if total_value < MENU[coffee]["cost"]:
                print("There is no money enough, coins refunded.")
            else:
                print("---------------------------------")
                print(f"\nYour {coffee} is ready. Enjoy!")

        else:
            print(f"\nCannot make {coffee}.")

        print("------------------------------------------------------")
        choose = input("Press 'Y' to choose a coffee or 'N' to exit: ").strip().upper()
        
        if choose == 'Y':
            clear_screen()
        elif choose == 'N':
            print("Leaving...")
            break
        else:
            print("Type a valid answer!")


main()


import os

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def operation_symbol(): 
    symbol = input("Pick an operation: ")
    while symbol not in operation:
        print("Type a valid answer!")
        symbol = input("Pick an operation: ")
    return symbol

operation = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }
def the_calculator():
    should_continue = True
    from improved_calculator_art import logo
    print(logo)
    n1 = float(input("What's the first number?\n"))
        
    while should_continue:
        for symbol in operation:
            print("__________")
            print(symbol)
        print("-----------")

        symbol = operation_symbol()
        n2 = float(input("What's the next number?\n"))
        calculation = operation[symbol]
        answer = calculation(n1, n2)# answer = operation[symbol](n1, n2)

        print(f"{n1} {symbol} {n2} = {answer}")
        exit = input("Another operation? (Y/N)\n").strip().upper()
        if exit == "N":
            should_continue = False
            print("leaving...")
        else:
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").strip().lower() == 'y':
                n1 = answer              
            else:
                should_continue = False
                clear_screen()
                the_calculator()

the_calculator()

import os
import secret_auction_art

participants_list = []

def participants_dictionary(nick, money):
    new_participant = {}
    new_participant["name"] = nick
    new_participant["dot"] = money
    participants_list.append(new_participant)

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def end():
    while True:
        print("------------------------------")
        match = input("Do you want to play again? (Y/N)\n").upper().strip()
        if match == "Y":
            main()
        elif match == "N":
            print("Leaving...")
            break
        else:
            print("Type a valid answer!")

def main():
    end = False
    choose = "y"
    while choose == "y":
        clear_screen()
        print(secret_auction_art.logo)
        print("Welcome to the Secret Auction!")
        print("------------------------------")
        name = input("Type your name: ")
        dot = int(input("Type your dot: "))
        participants_dictionary(name, dot)
        choose = input("Do you want to add another participant?(y/n)\n").strip().lower()

    greater_dot = None
    for i in participants_list:
        if greater_dot is None or i["dot"] > greater_dot["dot"]:
            greater_dot = i

    if choose == "n":
        input("Press any key to reveal the winner...")
        clear_screen()
        print(secret_auction_art.trophy)
        if greater_dot:
            print(f"The winner is {greater_dot['name']}, with ${greater_dot['dot']} dot.")
        else:
            print("No participants in the auction.")
main()
end()
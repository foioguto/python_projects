import os
import random
from blackjack_art import logo, trophy

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
            clear_screen()
            the_game()
            break
        elif match == "N":
            print("Leaving...")
            break
        else:
            print("Type a valid answer!")

def calculate_sum(hand):
    total = sum(hand)
    ace_count = hand.count(11)#count the number of aces in the hand
    
    while total > 21 and ace_count:
        total -= 10 #ace = 1
        ace_count -= 1 # 1 less ace
    
    return total

def the_game():
    print(logo)
    print("\nWelcome to the BlackJack game!")
    print("------------------------------")
    input("Press any key to start...")
    clear_screen()

    end_game = False
    
    while not end_game:
        print(logo)
        
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        user_hand = [random.choice(cards), random.choice(cards)]
        computer_hand = [random.choice(cards), random.choice(cards)]
        
        user_sum = calculate_sum(user_hand)
        computer_sum = calculate_sum(computer_hand)
        
        print(f"Your hand: {user_hand}, sum: {user_sum}")
        print("\n----------- VS ------------\n")
        print(f"Computer's hand: [{computer_hand[0]}, '?']\n")

        while user_sum < 21:
            decision = input("Press 'Y' to draw a card or 'N' to hold your hand: ").strip().upper()
            if decision == 'Y':
                user_hand.append(random.choice(cards))
                user_sum = calculate_sum(user_hand)
                print(f"Your hand: {user_hand}, sum: {user_sum}")
            else:
                break
        
        while computer_sum < 17:
            computer_hand.append(random.choice(cards))
            computer_sum = calculate_sum(computer_hand)
        
        print(f"\nYour hand: {user_hand}, sum: {user_sum}")
        print(f"Computer's hand: {computer_hand}, sum: {computer_sum}")
        
        if user_sum > 21:
            clear_screen()
            print(logo)
            print("\nYou Lose!")
            print(f"\nYour hand: {user_hand}, sum: {user_sum}")
            print("------------------------------------------")
            print(f"Computer's hand: {computer_hand}, sum: {computer_sum}")
        elif computer_sum > 21 or user_sum > computer_sum:
            clear_screen()
            print(trophy)
            print("\nYou Win!")
            print(f"\nYour hand: {user_hand}, sum: {user_sum}")
            print("------------------------------------------")
            print(f"Computer's hand: {computer_hand}, sum: {computer_sum}")
        elif user_sum < computer_sum:
            clear_screen()
            print(logo)
            print("\nYou Lose!")
            print(f"\nYour hand: {user_hand}, sum: {user_sum}")
            print("------------------------------------------")
            print(f"Computer's hand: {computer_hand}, sum: {computer_sum}")
        else:
            clear_screen()
            print(logo)
            print("\nDraw!")
            print(f"\nYour hand: {user_hand}, sum: {user_sum}")
            print("------------------------------------------")
            print(f"Computer's hand: {computer_hand}, sum: {computer_sum}")
        end_game = True
        end()

the_game()

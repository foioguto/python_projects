import os
import random
from secret_number_art import logo, trophy

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def end():
    while True:
        print("---------------------------------------")
        match = input("Press 'Y' to play again or 'N' to exit: ").strip().upper()
        if match == 'Y':
            clear_screen()
            main()
            break
        elif match == 'N':
            print("Leaving...")
            break
        else:
            print("\nType a valid answer!")

def main():
    print(logo)
    print("Welcome to the Secret Number game!")
    print("----------------------------------")
    input("Press any key to start...")
    clear_screen()
    print(logo)
    difficult = input("Choose the difficult, easy or hard?\n").strip().lower()
    if difficult == 'easy':
        lifes = 10
    elif difficult == 'hard':
        lifes = 5
    else:
        print("Type a valid answer!")
        return
    clear_screen()
    print(logo)

    answer = random.randint(1, 100)
    should_continue = True

    while should_continue and lifes > 0:
        guess = int(input("Guess a number between 1 and 100: ").strip())
        if guess == answer:
            lifes += 1
            clear_screen()
            print(trophy)
            print("You win!")
            should_continue = False
        elif guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
        
        lifes -= 1
        
        if lifes > 0 and should_continue:
            print(f"{lifes} lifes remaining.")
        elif lifes == 0:
            clear_screen()
            print(logo)
            print("You lose!")
            print(f"The number was {answer}.")
            should_continue = False
    end()
main()
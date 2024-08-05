import os
import random
from higher_lower_art import logo, vs, trophy
from higher_lower_data import data


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def end():
    while True:
        match = input("Type 'Y' to play again or 'N' to exit: ").strip().upper()
        if match == 'Y':
            clear_screen()
            main()
            break
        elif match == 'N':
            print("Leaving...")
            break
        else:
            print("Type a valid answer!")


def random_a():
    char_a = random.choice(data)
    data.remove(char_a)
    return char_a


def random_b():
    char_b = random.choice(data)
    data.remove(char_b)
    return char_b


def main():
    print(logo)
    print("\nWelcome to the Higher Lower game!")
    print("--------------------------------")
    input("Press any key to continue...")
    
    char_a = random_a()
    char_b = random_b()

    hits = 0
    should_continue = True
    while should_continue:
        higher = ""
        if char_a['follower_count'] > char_b['follower_count']:
            higher = char_a['name']
        else:
            higher = char_b['name']

        clear_screen()
        print(logo)
        print("Get 5 hits to win!")
        print(f"Hits: {hits}")
        print("--------------------------------------------------------------------")
        print(f"A: {char_a['name']}, {char_a['description']}, {char_a['country']}. ")
        print(vs)
        print(f"B: {char_b['name']}, {char_b['description']}, {char_b['country']}. ")
        print("--------------------------------------------------------------------")
        guess = input("Guess who have more followers, 'A' or 'B'? ").strip().upper()

        if guess == 'A':
            char_b = random_b()
            if char_a['name'] in higher:
                hits += 1
                print("You got it right!")
                input("Press any key to continue...")
            
            else:
                print("You missed!")
                should_continue = False
        
        elif guess == 'B':
            char_a = random_a()
            if char_b['name'] in higher:
                hits += 1
                print("You got it right!")
                input("Press any key to continue...")
            else:
                print("You missed!")
                should_continue = False
        else:
            print("Type a valid answer!")
            input("Press any key to continue...")

        if hits == 5:
            clear_screen()
            print(trophy)
            print("You win!")
            print("----------------------------")
            should_continue = False

    end()


main()




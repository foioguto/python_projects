import random
import Hangman_dataset

def end():
    while True:
        match = input("Do you want to play again? (Y/N)\n").upper().strip()
        if match == "Y":
            start()
        elif match == "N":
            print("Leaving...")
            break
        else:
            print("Type a valid answer!")

def start():
    from Hangman_art import logo
    print(logo)
    print("\n\nWelcome to the Hangman game!")
    print("----------------------------")
    input("Press any key to continue...")
    Hangman_dataset.clear_screen()

    word_list = []
    word_list.append(random.choice(Hangman_dataset.foods).strip().lower())
    word_str = "".join(map(str, word_list))
    blanks = ["_"] * len(word_str)

    print("The theme is food. Good luck!\n")
    print(" ".join(blanks))
    print("\n\n")

    end = False
    attempts = 6
    guessed_letter = []

    while not end:
        guess = Hangman_dataset.user_letter()

        if guess in guessed_letter:
            print("You already guessed that letter. Try again.")
            continue
        if guess in word_str:
            print("Right")
            for index, letter in enumerate(word_str):
                if letter == guess:
                    blanks[index] = guess
        else:
            print("Wrong")
            attempts -= 1
        guessed_letter.append(guess)

        input("Press any key to continue")
        Hangman_dataset.clear_screen()
        print("The theme is food, good luck!\n")
        print(" ".join(blanks))
        print(f"\nAttempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letter)}")
        print("\n\n")

        if "_" not in blanks:
            print("Congratulations! You have guessed the word!")
            end = True
        elif attempts == 0:
            print(f"Game Over! The word was: {word_str}")
            end = True
        from Hangman_art import stages
        print(stages[attempts])
start()
end()
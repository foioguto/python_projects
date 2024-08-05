import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("\nWelcome to the Caesar Cipher!")
    print("-------------------------------")
    selector = int(input("Type 1 to encode or 2 to decode:\n"))#'Try' command to avoid ValueError
    return selector

selector = menu()#It must be a global variable

def encode(plain_text, shift_amount):
    plain_text = str(input("Type a text to be encoded:\n").lower())
    shift_amount = int(input("Type the shift number:\n").strip())
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is: {cipher_text}")

def decode(plain_text, shift_amount):
    plain_text = str(input("Type a text to be decoded:\n").lower())
    shift_amount = int(input("Type the shift number:\n").strip())
    decoded_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            decoded_text += new_letter
        else:
            decoded_text += letter
    print(f"The decoded text is {decoded_text}")

if selector == 1:
    encode(plain_text="", shift_amount="")
elif selector == 2:
    decode(plain_text="", shift_amount="")
else:
    while selector != 1 or 2:
        print("\nType a valid answer!")
        input("Press any key to return to Menu...")
        clear_screen()
        selector = menu()

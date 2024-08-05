import random
import os

print("======================================")
print("| Welcome to the password generator! |")
print("======================================")
input("Press any key to continue...")
def clear_screen(): 
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

clear_screen()

upLetters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowLetters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

upLetters = int(input("How many uppercase letters would you like in your password? (Maximum 5)\n"))
clear_screen()
lowLetters = int(input("How many lowercase letters would you like in your password? (Maximum 5)\n"))
clear_screen()
symbols = int(input("How many symbols would you like in your password? (Maximum 5)\n"))
clear_screen()
numbers = int(input("How many numbers would you like in your password? (Maximum 5)\n"))
clear_screen()

password_list = []

for char in range(upLetters):
    password_list.append(random.choice(upLetters_list))
for char in range(lowLetters):
    password_list.append(random.choice(lowLetters_list))
for char in range(symbols):
    password_list.append(random.choice(symbols_list))
for char in range(numbers):
    password_list.append(random.choice(numbers_list))

random.shuffle(password_list)

password = ''.join(map(str, password_list))#map(function, iterable, ...)
#join = concatenate a sequence of strings
print("Generated password:  ", password)
print("\n\n\n\n\n\n\n")

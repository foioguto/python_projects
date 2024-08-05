import random

question = input("Welcome to the coinflipper. Do you bet on heads or tails?\n").strip().lower()

heads = "heads"
tails = "tails"

answer = random.randint(0, 1)

result = heads if answer == 0 else tails

if question == result:
    print(f"The result is {result}, you win!")
else:
    print(f"The result is {result}, you lost!")

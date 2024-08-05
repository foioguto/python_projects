import os

print("------------------------------")
print("Welcome to the BMI calculator!")
print("------------------------------")

input("Press any key to continue...")
def clear_screen(): # It is a function. Can have return or not.
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

clear_screen()

height = float(input("Enter your height in meters: "))
height = round(height, 2)
weight = float(input("Enter your weight in kilograms: "))
weight = round(weight, 1)

bmi = weight / height**2
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your Bmi is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your Bmi is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"You BMI is {bmi}, you are clinically obese.")
#Note: I would make just one comparasion in if statement,
# like line 26, elif bmi < 25:
# It would be the same.
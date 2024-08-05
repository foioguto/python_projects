print("+-----------------------------------------+")
print("| Welcome to the Ultimate Bill Calculator |")
print("+-----------------------------------------+")

bill = float(input("What was the total bill?\nIt was: $"))
tip = int(input("What the percentage would you like to give? 10, 12 or 15?\n"))

percentage_tip = tip /100 

people = int(input("how many people to split the bill?\n"))

total = (bill * percentage_tip + bill) /people 
total = round(total, 2)

print(f"Each person should pay ${total}")


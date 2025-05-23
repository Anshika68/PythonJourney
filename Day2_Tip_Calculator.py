# Day 2 - Tip Calculator
print("Welcome to the tip calculator!\n")
amount = int(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_amount = (amount * tip_percent) / 100
total_amount  = amount + tip_amount
each_person_amount = total_amount / number_of_people
print(f"Each person should pay: {each_person_amount}")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
letter_count = int(input("How many letters would you like in your password?\n"))
numbers_count = int(input("How many symbols would you like?\n"))
symbols_count = int(input("How many numbers would you like?\n"))

letters_choices = random.choices(letters, k=letter_count)
numbers_choices = random.choices(numbers, k=numbers_count)
symbols_choices = random.choices(symbols, k=symbols_count)

password_list = letters_choices + numbers_choices + symbols_choices
print(password_list)
random.shuffle(password_list)
print(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")

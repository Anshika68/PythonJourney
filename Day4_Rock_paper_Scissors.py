import random
choice = int(input("What do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissors: "))
action_dict = {0: "rock", 1: "paper", 2: "scissors"}
possible_choices = [0,1,2]
print(f"Your choice: \n{action_dict[choice]}")
computer_choice = random.choice(possible_choices)
print(f"Computer choice: \n{action_dict[computer_choice]}")
if choice == computer_choice:
  print("DRAW")
elif (choice < 1 and computer_choice > 1) or (choice == 1 and computer_choice < 1) or (choice>1 and computer_choice == 1):
  print("You Win")
else:
  print("You lose")

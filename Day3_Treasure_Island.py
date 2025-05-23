print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
print("You're at a cross roads. Where do you want to go?\n")
action = input("\tType \"left\" or \"right\"\n")
if action != "left":
  print("Fall into a hole.\nGame Over.")
else:
  print("You've come to a lake. There is an island in the middle of the lake.\n")
  action = input("Type \"swim\" to swin across or \"wait\" to wait for boat\n")
  if action != "wait":
    print("Attacked by trout.\nGame Over.")
  else:
    print("You have arrived at the island unharmed. There is house with 3 doors.\n")
    action = input("One red, one yellow and one blue. Which colour do you choose\n")
    if action == "red":
      print("Burned by fire.\nGame Over.")
    elif action == "yellow":
      print("You Win!")
    elif action == "blue":
      print("Eaten by beasts.\nGame Over.")
    else:
      print("Game Over.")

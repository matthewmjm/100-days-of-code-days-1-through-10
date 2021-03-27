import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opponent = random.randint(1, 3)
yourself = int(input("What do you choose? Type 1 for Rock, 2 for Paper, and 3 for Scissors.\n"))

if opponent == 1:
    opponent_choice = rock
elif opponent == 2:
    opponent_choice = paper
else:
    opponent_choice = scissors

if yourself == 1:
    yourself_choice = rock
elif yourself == 2:
    yourself_choice = paper
else:
    yourself_choice = scissors

print(yourself_choice)
print("\nComputer chose:\n")
print(opponent_choice)

if yourself == 1:
    if opponent == 1:
        print("It is a DRAW!")
    elif opponent == 2:
        print("You LOSE!")
    else:
        print("You WIN!")
elif yourself == 2:
    if opponent == 1:
        print("You WIN!")
    elif opponent == 2:
        print("It is a DRAW!")
    else:
        print("You LOSE!")        
else:
    if opponent == 1:
        print("You LOSE!")
    elif opponent == 2:
        print("You WIN!")
    else:
        print("It is a DRAW!")
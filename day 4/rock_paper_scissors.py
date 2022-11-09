import random
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

#Write your code below this line 👇
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
else:
    print(scissors)

random = random.randint(0, 2)
print("Computer choose:")
if random == 0:
    print(rock)
elif random == 1:
    print(paper)
else:
    print(scissors)

if choose == 0 and random == 2:
    print("You win")
elif choose == 0 and random == 1:
    print("You lose")
elif choose == 1 and random == 0:
    print("You win")
elif choose == 1 and random == 2:
    print("You lose")
elif choose == 2 and random == 1:
    print("You win")
elif choose == 2 and random == 0:
    print("You lose")
else:
    print("Drawn!")
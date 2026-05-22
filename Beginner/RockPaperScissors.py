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



choicelist = [rock, paper, scissors]

print('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors')
choice = int(input())
computer_choice = random.randint(0,2)

if (choice < 3 and choice >= 0):
    print(choicelist[choice])
    print('Computer chose: ')
    print(choicelist[computer_choice])

if choice >= 3 or choice < 0:
    print('Invalid Number. Try Again')
elif choice == computer_choice:
    print("Its a draw")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win")
else:
    print("You Lose")

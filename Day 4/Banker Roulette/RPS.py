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

indexes = [rock, paper, scissors]
userInput = input('Please enter any value from 0 = Rock, 1 = Paper and 2 = Scissors\n')
userChoice = int(userInput)
computerChoice = random.randint(0, 2)

if userChoice <= -1 or userChoice >= 3:
    print('Enter valid choices')
elif userChoice ==  computerChoice :
    print('It\'s a draw')
elif userChoice == 2 and computerChoice == 0:
    print('You win, Rock beats Scissors')
elif userChoice == 0 and computerChoice == 1:
    print('You win, Paper beats Rock')
elif userChoice == 1 and computerChoice == 2:
    print('You win, Scissors beats Paper')
else: print('You lost mate, try again...')
print(f'Output: {indexes[computerChoice]} and you chose {indexes[userChoice]}')

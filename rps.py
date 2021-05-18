import random

beats = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
user = input('What you play? ')
comp = random.choice(['rock', 'paper', 'scissors'])

print('You played', user)
print('I played', comp)

if user == comp:
    print("It's a draw.")
elif user == beats[comp]:
    print('You win.')
else:
    print('I win.')

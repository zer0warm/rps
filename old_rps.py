import random

user = input('What you play? ')
comp = random.choice(['rock', 'paper', 'scissors'])

print('You played', user)
print('I played', comp)

if ((user == 'rock' and comp == 'scissors')
        or (user == 'paper' and comp == 'rock')
        or (user == 'scissors' and comp == 'paper')):
    print('You win.')
elif user == comp:
    print("It's a draw.")
else:
    print('I win.')

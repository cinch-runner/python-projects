"""
Rock, paper, scissors
"""

import random

options = ['rock', 'paper', 'scissors']
comp_guess = random.choice(options)
result = 'Player wins!'

while True:
    user_guess = input('Please type rock, paper, or scissors: ').lower()

    if user_guess == comp_guess:
        result = 'It\'s a tie!'
        break
    elif comp_guess == 'rock' and user_guess == 'scissors':
        result = 'The computer wins!'
    elif comp_guess == 'scissors' and user_guess == 'paper':
        result = 'The computer wins!'
    elif comp_guess == 'paper' and user_guess == 'rock':
        result = 'The computer wins!'
    break

print(f'The computer chose {comp_guess} and the player chose {user_guess}', '\n', result)
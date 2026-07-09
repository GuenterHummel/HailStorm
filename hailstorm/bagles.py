"""Bagels, by Al Sweigart a@invent with python.com
A deductive logic game where you must guess a number based on clues.
View the code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game puzzle
"""

import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100.

def main():
    print('''Bagels, a deductive logic game, 
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
  Pico          One digit is correct but in teh wrong position.
  Fermi         One digit is correct and in the right position.
  Bagels        No digit is correct.
  
For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True: #Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print ('I have thought of a secret number.')
        print (' You have {} guesses to get it.'.format (MAX_GUESSES))

        numGuesses = 1

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list ('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
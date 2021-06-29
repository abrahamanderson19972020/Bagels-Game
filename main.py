import random


def main():
    print("""In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
    The game offers one of the following hints in response to your guess:

    “Pico” when your guess has a correct digit in the wrong place, 

    “Fermi” when your guess has a correct digit in the correct place, 

    “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.""")

    secret_number = str(random.randint(100, 1000))
    count = 0
    guess_limit = 10

    print(f"print(' You have {guess_limit} guesses to get it.'")

    while count < guess_limit:

        guess = input("Enter Your Guess :")
        count += 1
        clues = getClues(guess, secret_number)
        print(clues)


    else:
        print("You lose!")
        print(f'The answer was {secret_number}.')


def getClues(guess, secret_number):
    if guess == secret_number:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_number:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


if __name__ == '__main__':
    main()



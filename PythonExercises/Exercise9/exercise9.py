# Exercise 9

import random
import time
import re

pattern = r"^[-+]?[0-9]+$"  # Pattern to find positive or negative or zero integer.
exit_keys = ("n", "e", "ex", "exi", "exit")  # Use these keys to exit.
play_again = True  # Boolean to restart the game after finishing.
user_input = None

while play_again is True and user_input not in exit_keys:
    print('Please wait while the machine generates a random number...')
    time.sleep(0.6)
    random_number = random.randint(1, 9)  # Generate a random integer between 1 and 9.
    print('---> A random integer number was generated between 1 and 9. Try to guess it.' + ' *** ' + str(random_number) + ' *** ')
    number_of_guesses = 0
    while True:  # Loop forever or until exit key is typed.
        user_input = input('---> Your guess: ')  # Get user input.
        if user_input in exit_keys:  # User just entered on of the exit sequences. ('n', 'e', 'ex', 'exi', 'exit')
            user_input_on_exit = input('You just pressed one of the exit keys (n, e, ex, exi, exit)...\nAre you sure you want to exit (y/n)? ')
            if user_input_on_exit == 'y':
                print('Exiting...')
                print(100 * '_' + '\n')
                exit(0)
            else:
                continue
        elif not re.match(pattern, user_input):  # User did not enter an integer.
            print(18 * ' ' + 'Warning! Please type an integer. (This will not count as a valid guess. Lucky you...)')
            continue
        guess = int(user_input)
        if guess < random_number:  # User's guess was lower than the number generated.
            number_of_guesses += 1
            print(18 * ' ' + ' Too low... Please try again.')
        elif guess > random_number:  # User's guess was higher than the number generated.
            number_of_guesses += 1
            print(18 * ' ' + ' Too high... Please try again.')
        elif random_number == int(user_input):  # User's guessed correctly.
            number_of_guesses += 1
            print((len(str(number_of_guesses)) + 23) * ' ' + 81 * '*')
            print(19 * ' ' + ' --> * Congratulations!!! your guess was Correct and you only needed ' + str(number_of_guesses) + ' guess/guesses * <--')
            print((len(str(number_of_guesses)) + 23) * ' ' + 81 * '*' + '\n')
            break
    user_input = input('Would you like to play again (y/n)? ')  # Prompt player to restart the game.
    if user_input == 'y':
        print('Restarting...')
        time.sleep(0.6)
        print(100 * '_' + '\n')
        continue
    elif user_input == 'n':
        print('Exiting...')
        print(100 * '_' + '\n')
        play_again = False

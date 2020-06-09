# Exercise 2

import re

pattern = r'^[-+]?[0-9]+$'  # Pattern for positive or negative integer.
exit_keys = ('n', 'e', 'ex', 'exi', 'exit')  # Use these keys to exit.
while True:
    # Wait for user input.
    # '\033[61D' moves the cursor 61 positions to the left.
    user_input = input('\nPlease, type an integer number and press enter:' +
                       15*' ' +
                       '|Use these keys to exit: ' +
                       str(exit_keys) +
                       '|' +
                       '\033[61D')
    # User just entered on of the exit sequences.
    # 'n', 'e', 'ex', 'exi', 'exit'.
    if user_input in exit_keys:
        user_input_on_exit = input('\nYou just pressed one of the exit keys '
                                   '(n, e, ex, exi, exit)...\n'
                                   'Are you sure you want to exit (y/n)? ')
        if user_input_on_exit == 'y':
            print('Exiting...')
            print(100 * '_')
            break
        else:
            continue
    # User input, matches 'pattern' (namely is an integer).
    elif re.match(pattern, user_input):
        int_value = int(user_input)  # Convert to int type.
        # Integer is even.
        if int_value % 2 == 0:
            print('You just typed an even integer.')
            if int_value % 4 == 0:  # Integer is even and a multiple of 4.
                print('This integer is a multiple of 4.')
        # Integer is odd.
        else:
            print('You just typed an odd integer.')
        print(100 * '_')
    # User input is not valid integer type.
    else:
        print('The value you just typed is not an integer. '
              'Please, try again.')


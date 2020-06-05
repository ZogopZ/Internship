# Exercise 10

import random


exit_keys = ("n", "e", "ex", "exi", "exit")  # Use these keys to exit.


while True:  # Loop forever or until exit key is typed.
    print(44 * '-')
    print('exit keys: ', exit_keys)
    print(44 * '-')
    print('\nPlease wait while the machine generates two random lists...')
    alpha = random.choices(range(0, 100), k=random.randint(0, 100))  # Generate a list of random 'k' length with random integers in range 0-100.
    beta = random.choices(range(0, 100), k=random.randint(0, 100))  # Generate a list of random 'k' length with random integers in range 0-100.
    print('The machine generated two random lists with integers.')
    print(4 * ' ' + 'List alpha ->', alpha)
    print(4 * ' ' + 'List beta ->', beta)
    user_input = input('\n---> Press enter to continue or one of the exit keys to exit.\n     This will return common elements from the above lists, without duplicates: ')
    if user_input == '':  # Empty 'user_input' means that the user pressed enter without any other input.
        common_elements_list = list(dict.fromkeys([alpha_x for alpha_x in alpha if alpha_x in beta]))  # Find common elements and remove duplicates.
        print('\n---> common elements', common_elements_list)
        valid_input = True
        while valid_input is True:
            user_input = input('Would you like to restart (y/n)? ')  # Prompt player to restart the process.
            if user_input == 'y':
                print('Restarting...')
                print(100 * '_')
                valid_input = False  # Used to break the 'while' loop.
            elif user_input == 'n':
                print('Exiting...')
                print(100 * '_')
                exit(0)
            else:
                print('Sorry I didn\'t get that...')  # 'while' loop will continue.
    elif user_input in exit_keys:  # User just entered on of the exit sequences. ('n', 'e', 'ex', 'exi', 'exit')
        user_input_on_exit = input('\nYou just pressed one of the exit keys (n, e, ex, exi, exit)...\nAre you sure you want to exit (y/n)? ')
        if user_input_on_exit == 'y':
            print('Exiting...')
            print(100 * '_' + '\n')
            exit(0)
        else:
            continue

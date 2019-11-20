# Exercise 2

import re

pattern = r"^[-+]?[0-9]+$"  # Pattern to find positing or negative integer.
exit_keys = ("n", "e", "ex", "exi", "exit")     # Use these keys to exit.
print("Exit keys: n, e, ex, exi, exit. Type key + Enter to exit")

while True: # Loop forever or until exit key is typed.
    prompt = "Please, type an integer number and press enter"
    user_input = input(prompt + 50*" " + "exit keys: " + str(exit_keys) + "\n")     # Get user input.

    if user_input in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("Program will now exit. Thank you.")
        break
    if re.match(pattern, user_input):   # User input, matches pattern (namely is an integer).
        int_value = int(user_input)     # Convert to int type.
        if int_value % 2 == 0:          # Integer is even.
            print("You just typed an even integer.")
            if int_value % 4 == 0:      # Integer is even and a multiple of 4.
                print("This integer is a multiple of 4\n")
            print("")
        else:                           # Integer is odd.
            print("You just typed an odd integer.\n")
    else:                               # User input is not valid integer type.
        print("The value you just typed is not an integer. Please, try again.\n")

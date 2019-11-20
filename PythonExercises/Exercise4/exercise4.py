# Exercise 4

import re

pattern = r"^[-+]?[0-9]+$"  # Pattern to find positive or negative integer.
exit_keys = ("n", "e", "ex", "exi", "exit")     # Use these keys to exit.
print("Type exit key + Enter to exit" + 67*" " + "||exit keys: " + str(exit_keys) + "||\n")

while True:     # Loop forever or until exit key is typed.
    prompt = "Please, type an integer number and press enter"
    user_input = input(prompt + 50*" " + "||exit keys: " + str(exit_keys) + "||\n")     # Get user input.
    answer_list = []

    if user_input in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("---> Program will now exit. Thank you.")
        break
    if re.match(pattern, user_input):   # User input, matches pattern (namely is an integer).
        int_value = int(user_input)     # Convert to int type.
        if int_value == 0:
            print("---> Hey all non-zero numbers are divisors of 0.\n")
            continue;
        elif int_value > 0:
            for potential_divisor in range(1, int(int_value + 1 / 2)):
                if int_value % potential_divisor == 0:
                    answer_list.append(potential_divisor)
            answer_list.append(int_value)
        elif int_value < 0:
            for potential_divisor in range(int(int_value - 1 / 2), 0):
                if int_value % potential_divisor == 0:
                    answer_list.append(potential_divisor)

        print("---> " + str(answer_list) + "\n")

    else:                               # User input is not valid integer type.
        print(" The value you just typed is not an integer. Please, try again.\n")

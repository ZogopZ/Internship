# Exercise 7

import random
import re


pattern = r"[-+]?[0-9]+"  # Pattern to find positive or negative integers.
exit_keys = ("n", "e", "ex", "exi", "exit")     # Use these keys to exit.
auto_keys = ("a", "au", "aut", "auto")  # Use these keys to automatically generate a list of random integers.
print("Type exit key + Enter to exit" + 67*" " + "||exit keys: " + str(exit_keys) + "||\n")

while True:     # Loop forever or until exit key is typed.
    prompt = "Please, type a few integers and press enter...\n" \
             "or type a and press enter to automatically generate a list of integers."
    user_input = input(prompt + 25 * " " + "||exit keys: " + str(exit_keys) + "||\n")     # Get user input.

    if user_input in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("---> Program will now exit. Thank you.")
        break
    elif user_input in auto_keys:   # If user typed one of the auto keys.
        a_len = random.randrange(20)  # Generate a random integer to represent the length of list a.
        a = random.sample(range(1, 101), a_len)
        # Generate a list of a_len length with random integers in range 1-100.
        print(str(a) + " <--- Automatically generated list.")
        print(str([even for even in a if even % 2 == 0]) + " <--- Even numbers of the above list.\n")
        continue
    elif user_input not in auto_keys:
        user_input_list = [int(value) for value in re.findall(pattern, user_input)]
        # Find all integer values in user's input and add them to user_input_list.
        print(str(user_input_list) + " <--- User input list.")
        print(str([even for even in user_input_list if even % 2 == 0]) + " <--- Even numbers of the above list.\n")

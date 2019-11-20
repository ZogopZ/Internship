# Exercise 3

import re

pattern1 = r"[-+]?[0-9]+"    # Pattern to find positive or negative integer.
pattern2 = r"^[-+]?[0-9]+$"  # Pattern to find one positive or negative integer.
exit_keys = ("n", "e", "ex", "exi", "exit")     # Use these keys to exit.
print("\nExit keys: n, e, ex, exi, exit.\nType key + Enter to exit\n")

while True:     # Loop forever or until exit key is typed.

    prompt_list = "Please, type some integers, separated by space and press enter."
    user_input_list = input(prompt_list + 50*" " + "exit keys: " + str(exit_keys) + "\n")
    # Get user's input. List of integers to be parsed.
    if user_input_list in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("Program will now exit. Thank you.")
        break
    user_list = [int(value) for value in re.findall(pattern1, user_input_list)]
    # Find all valid integers in user's input list.

    prompt_number = "Please, type a number to compare to list's values and press enter."
    user_input_number = input(prompt_number + 47*" " + "exit keys: " + str(exit_keys) + "\n")
    # Get user's input. Number to be compared with each list item.
    if user_input_list in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("Program will now exit. Thank you.")
        break
    user_number = int(re.match(pattern2, user_input_number).group())
    # Find valid integer in user's input.

    print([number for number in user_list if number < user_number])     # One-liner.

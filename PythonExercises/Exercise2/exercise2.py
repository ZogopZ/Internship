# Exercise 2

import re

pattern = r"^[-+]?[0-9]+$"
exit_keys = ("n", "e", "ex", "exi", "exit")
print("Exit keys: n, e, ex, exi, exit. Type key + Enter to exit")

while True:
    prompt = "Please, type an integer number and press enter: "
    user_input = input(prompt)

    if user_input in exit_keys:
        print("Program will now exit. Thank you.")
        break
    if re.match(pattern, user_input):
        int_value = int(user_input)
        if int_value % 2 == 0:
            print("You just typed an even integer.\n")
        else:
            print("You just typed an odd integer.\n")
    else:
        print("The value you just typed is not an integer. Please, try again.\n")

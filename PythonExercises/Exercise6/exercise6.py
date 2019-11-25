# Exercise 6

exit_keys = ("n", "e", "ex", "exi", "exit")     # Use these keys to exit.
print("Type exit key + Enter to exit" + 67*" " + "||exit keys: " + str(exit_keys) + "||\n")

while True:     # Loop forever or until exit key is typed.
    prompt = "Please, type a string and press enter"
    user_input = input(prompt + 50*" " + "||exit keys: " + str(exit_keys) + "||\n")     # Get user input.

    if user_input in exit_keys:     # If user typed one of the exit keys, program will exit.
        print("---> Program will now exit. Thank you.")
        break
    if user_input == user_input[::-1]:
        # Compare the user's string with itself reversed, to find out whether it is a palindrome or not.
        print("---> The string you typed is a palindrome!")
    else:
        print("---> The string you typed is NOT a palindrome...")
    print("")

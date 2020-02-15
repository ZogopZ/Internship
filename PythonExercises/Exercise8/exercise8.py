# Exercise 8

import random
from PythonExercises.Exercise8.Tools import find_result

exit_keys = ("n", "e", "ex", "exi", "exit")  # Use these keys to exit.
rock_keys = ("r", "ro", "roc", "rock")  # Use these keys to play rock.
paper_keys = ("p", "pa", "pap", "pape", "paper")  # Use these keys to play paper.
scissor_keys = ("s", "sc", "sci", "scis", "sciss",
                "scisso", "scissor", "scissors")  # Use these keys to play scissors.

while True:  # Loop forever or until exit key is typed.
    prompt = "Please select a game mode:\n" \
             " ---> press a and enter for bot mode.\n" \
             " ---> press pvp and enter for player versus player."
    user_input = input(prompt + 25 * " " + "||exit keys: " + str(exit_keys) + "||\n")  # Get user input.

    if user_input in exit_keys:  # If user typed one of the exit keys, program will exit.
        print("---> Program will now exit. Thank you.")
        break
    elif user_input == "a":
        score_a = 0
        score_b = 0
        print(" " + 70 * "_")
        while user_input not in exit_keys:
            bot_A_selection = random.choice(["rock", "paper", "scissors"])
            bot_B_selection = random.choice(["rock", "paper", "scissors"])
            print("|Player A selects --> |%s|" % bot_A_selection.center(8) + 39*" " + "|")
            print("|Player B selects --> |%s|" % bot_B_selection.center(8) + 39*" " + "|")
            result = find_result(bot_A_selection, bot_B_selection)

            if result == "tie":
                print("| ---> Tie no one scored!" + 46*" " + "|")
            elif result == "botA":
                score_a += 1
                print("| ---> Player A just scored a point." + 35*" " + "|")
            elif result == "botB":
                score_b += 1
                print("| ---> Player B just scored a point." + 35*" " + "|")
            print(str(score_a) + " " + str(score_b) + "\n"
                                                      "to continue press enter")
            user_input = input("")

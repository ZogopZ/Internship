def find_result(bot_a, bot_b):
    result = ""
    if bot_a == bot_b:
        result = "tie"

    elif bot_a == "rock" and bot_b == "paper":
        result = "botB"
    elif bot_a == "rock" and bot_b == "scissors":
        result = "botA"
    elif bot_b == "rock" and bot_a == "paper":
        result = "botA"
    elif bot_b == "rock" and bot_a == "scissors":
        result = "botB"

    elif bot_a == "paper" and bot_b == "rock":
        result = "botA"
    elif bot_a == "paper" and bot_b == "scissors":
        results = "botB"
    elif bot_b == "paper" and bot_a == "rock":
        result = "botB"
    elif bot_b == "paper" and bot_a == "scissors":
        result = "botA"

    elif bot_a == "scissors" and bot_b == "rock":
        result = "botB"
    elif bot_a == "scissors" and bot_b == "paper":
        result = "botA"
    elif bot_b == "scissors" and bot_a == "rock":
        result = "botA"
    elif bot_b == "scissors" and bot_a == "paper":
        result = "botB"

    return result
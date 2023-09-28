def guess_game(guess, number):
    if guess < number:
        num = -1
        return num
    elif guess > number:
        num = 1
        return num
    else:
        num = 0
        return num

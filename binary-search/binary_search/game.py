import random

number = random.randint(1, 100)


def guess_game(guess):
    if guess < number:
        num = -1
        return num
    elif guess > number:
        num = 1
        return num
    else:
        num = 0
        return num

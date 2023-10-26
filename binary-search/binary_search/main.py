import random
from game import guess_game, number
from search import binarysearch


def main():
    # number = random.randint(1, 100)
    array = list(range(1, 101))
    guess = binarysearch(
        array=array,
    )
    num = guess_game(guess)
    if num == 0:
        print("correct number was", guess)


main()

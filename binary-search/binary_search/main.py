import random
from game import guess_game, number
from search import binarysearch


def main():
    array = list(range(1, 101))
    low = 1
    high = len(array) - 1

    guess = binarysearch(array=array, low=low, high=high)
    num = guess_game(guess)
    if num == 0:
        print("correct number was", guess)


main()

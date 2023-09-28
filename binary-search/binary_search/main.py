import random
from game import guess_game
from search import binarysearch

array = list(range(1, 101))


def main():
    number = random.randint(1, 100)
    low = 1
    high = 100
    guess = binarysearch(low=low, high=high)
    num = guess_game(number=number, guess=guess)
    while num != 0:
        guess, high, low = binarysearch(low=low, high=high, num=num)
        num = guess_game(number=number, guess=guess)
    print("pigbp")
    print("correct number was", guess)


main()

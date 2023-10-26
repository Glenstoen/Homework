from game import guess_game


def binarysearch(array, low, high):
    mid = (low + high) // 2

    num = guess_game(mid)
    if num == 0:
        return mid
    if num == 1:
        return binarysearch(array, low, high=mid - 1)
    elif num == -1:
        return binarysearch(array, low=mid + 1, high=high)

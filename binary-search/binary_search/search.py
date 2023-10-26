# def binarysearch(array, x, low=1, high=100):
#      mid = (high + low) // 2
#      if array[mid] == x:
#         return mid
#    elif array[mid] > x:
#       return binarysearch(array=array, low=low, high=mid - 1, x=x)
##     return binarysearch(array=array, low=mid + 1, high=high, x=x)
from game import guess_game


def binarysearch(array, num=2):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2
    if num == 2:
        num = guess_game(mid)
    if num == 0:
        return mid
    if num == -1:
        num = guess_game(mid)
        return binarysearch(array[:mid], num)
    elif num == 1:
        num = guess_game(mid)
        return binarysearch(array[mid + 1 :], num) + (mid + 1)

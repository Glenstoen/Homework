def binarysearch(low, high, num=2):
    while low <= high:
        guess = low + (high - low) // 2
        if num == 1:
            high = guess - 1
            return guess, high, low
        if num == -1:
            low = guess + 1
            return guess, high, low
        return guess

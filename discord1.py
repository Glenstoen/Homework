from pprint import pprint


def soda_can():
    _intro = input("Hello, would you like to order a beverage? [Y/N]\n")
    current_stock = {
        "1": ["Coca cola", 10],
        "2": ["Pepsi", 4],
        "3": ["Pepsi max", 5],
        "4": ["Fanta", 2],
        "5": ["Fanta exotic", 2],
        "6": ["Solo", 1],
        "7": ["Solo Super", 7],
        "8": ["Urge", 9],
        "9": ["Villa", 8],
    }
    while True:
        print("These are your options")
        pprint(current_stock)
        order = input(
            "Please enter the number of the beverage you want or 'N' to exit:\n"
        )
        if order == "N":
            print("Okay, Have a nice day!")
            break
        if current_stock[order][1] == 0:
            print("Sorry, this is out of stock\n")
            continue
        current_stock[order][1] -= 1
        print("here is you", current_stock[order][0])


soda_can()
# hei

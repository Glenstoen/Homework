import string


def pw_val():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    numbers = string.digits
    while True:
        input_str = input(
            "input a password. the pasword MUST:\n1: Be at least 8 characters long.\n2: Contain minimum 1 upper case letter.\n3: Contain minimum 1 lower case letter.\n4: Contain minimum 1 number.\n5: Contain minimum 1 special character.\n"
        )
        if not len(input_str) >= 8:
            print("Your password must be at least 8 characters long\n")
            continue
        if not any(c in upper for c in input_str):
            print("Your password must contain at least one upper case letter\n")
            continue
        if not any(c in lower for c in input_str):
            print("Your password must contain at least one lower case letter\n")
            continue
        if not any(c in numbers for c in input_str):
            print("Your password must contain at least one number\n")
            continue
        if not any(c in special for c in input_str):
            print("Your password must contain a special Character\n")
            continue
        print("Good job, you password", input_str, "is APPROVED\n")
        return


pw_val()

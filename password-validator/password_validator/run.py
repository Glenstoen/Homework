import string


def pw_val():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    numbers = string.digits

    input_str = input(
        "input a password. the pasword MUST:\n1: Be at least 8 characters long.\n2: Contain minimum 1 upper case letter.\n3: Contain minimum 1 lower case letter.\n4: Contain minimum 1 number.\n5: Contain minimum 1 special character.\n"
    )
    if len(input_str) >= 8:
        if any(c in upper for c in input_str):
            if any(c in lower for c in input_str):
                if any(c in numbers for c in input_str):
                    if any(c in special for c in input_str):
                        print("Good Job, your password", input_str, " is approved")
                    else:
                        print("Your password must contain a special Character")
                else:
                    print("Your password must contain at least one number")
            else:
                print("Your password must contain at least one lower case letter")
        else:
            print("Your password must contain at least one upper case letter")
    else:
        print("Your password must be at least 8 characters long")


pw_val()

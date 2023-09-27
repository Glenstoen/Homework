def recurse_fac(x):
    if x == 1:
        return 1
    else:
        return (x * recurse_fac(x-1))
    
num = int(input("enter a number\n"))
result = recurse_fac(num)
print(f"the factorial of {num} is {result}")
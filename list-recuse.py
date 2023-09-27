def recurse_list(x):
    if len(x)==0:
        return 0
    else:
        return x[0] + recurse_list(x[1:])
print (f"sum of the list is {recurse_list([1,2,3,4,5])}")
def sum_all(*args): # can rename anything but args is conventional
    # print(*args) # prints all arguments
    # print(args) # prints a tuple containing all arguments
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
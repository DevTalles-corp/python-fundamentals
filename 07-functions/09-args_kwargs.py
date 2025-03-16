
def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0

    for item in kwargs.values():
        total += item

    return sum(args) + total


print(big_function(1, 2, 3, 4, 5, 6, 7, 8, 9, num1=77, num2=120))

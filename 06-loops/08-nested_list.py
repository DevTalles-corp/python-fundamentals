
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")
    print()

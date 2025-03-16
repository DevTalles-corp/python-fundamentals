
tax = 16


def change_global():
    global tax
    tax = 18
    return tax


print(tax)

print(change_global())
print(tax)


def outer():
    enclosing_variable = "Enclosing variable"

    def inner():
        nonlocal enclosing_variable
        enclosing_variable = "Enclosing Modificado"

    inner()
    print(enclosing_variable)


outer()

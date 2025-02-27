x = 10


def outer_function():
    x = 20

    def inner_function():
        print(x)  # Statically determined to be x in the enclosing scope

    return inner_function


f = outer_function()
f()  # Output: 20
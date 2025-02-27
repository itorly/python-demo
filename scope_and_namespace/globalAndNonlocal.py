# Global namespace
x = 10


def outer_function():
    # Enclosing namespace
    y = 20

    def inner_function():
        # Local namespace
        nonlocal y  # Refers to y in the enclosing namespace
        global x  # Refers to x in the global namespace
        y = 30  # Modifies y in the enclosing namespace
        x = 40  # Modifies x in the global namespace
        z = 50  # z is in the local namespace
        print("Inner function:", x, y, z)

    inner_function()
    print("Outer function:", x, y)


outer_function()
print("Global scope:", x)
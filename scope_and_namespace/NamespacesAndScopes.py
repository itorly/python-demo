# Global namespace
x = 10  # x is in the global namespace


def outer_function():
    # Enclosing namespace
    y = 20  # y is in the enclosing namespace

    def inner_function():
        # Local namespace
        z = 30  # z is in the local namespace
        print("Inner function:", x, y, z)  # Accessing x, y, z

    inner_function()
    print("Outer function:", x, y)  # Accessing x, y


outer_function()
print("Global scope:", x)  # Accessing x
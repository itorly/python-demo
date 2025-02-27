def outer_function():
    x = 10

    def inner_function():
        print(x)  # Dynamically resolves x from the enclosing scope

    inner_function()


outer_function()  # Output: 10
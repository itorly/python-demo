def create_counter():
    count = 0  # Local namespace for create_counter

    def counter():
        nonlocal count  # Refers to count in the enclosing namespace
        count += 1
        return count

    return counter


my_counter = create_counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3
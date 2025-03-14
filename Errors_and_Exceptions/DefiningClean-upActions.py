# 8.7. Defining Clean-up Actions
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
        return False

print( bool_return() )

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    # except TypeError:
    #     print("Please enter two numbers!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)


divide(2, 0)


divide("2", "1")

# 1.Exception handled by an except clause, and finally clause executes
def case_1():
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
    finally:
        print("Finally clause executed")

case_1()

# 2. Exception occurs in except or else clause, and finally clause executes
def case_2():
    try:
        result = 10 / 1  # No exception here
    except ZeroDivisionError:
        print("This won't be executed")
    else:
        print("Else clause executed")
        result = 10 / 0  # Exception occurs in else clause
    finally:
        print("Finally clause executed")

case_2()

# 3.  Finally clause executes a return statement, and exceptions are not re-raised
def case_3():
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
        raise  # Re-raise the exception
    finally:
        print("Finally clause executed")
        return "Returned from finally"  # This suppresses the exception

print(case_3())

# 4. Try statement reaches a break, continue, or return, and finally clause executes
def case_4():
    try:
        print("Try clause executed")
        return "Returned from try"  # Try clause returns
    finally:
        print("Finally clause executed")

print(case_4())

# 5. Finally clause includes a return statement, overriding the try clause's return
def case_5():
    try:
        print("Try clause executed")
        return "Returned from try"  # Try clause returns
    finally:
        print("Finally clause executed")
        return "Returned from finally"  # This overrides the try's return

print(case_5())
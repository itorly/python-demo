# Function Examples
def foo(name, /, **kwds):
    return 'name' in kwds

print( foo(1, **{'name': 2}) )

# Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

print( concat("earth", "mars", "venus") )

print(concat("earth", "mars", "venus", sep="."))

# Unpacking Argument Lists
print(list(range(3, 6)))      # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))         # call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))

# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
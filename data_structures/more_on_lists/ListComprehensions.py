# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
numbers = [num for elem in vec for num in elem]
print(numbers)

# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

t = 12345, 54321, 'hello!'
x, y, z = t
print(x, y)

a = set('abracadabra')
b = set('alacazam')
print('a=', a)                                 # unique letters in a
print('b=', b)                                 # unique letters in a

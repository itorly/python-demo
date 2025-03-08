# 7.1. Fancier Output Formatting
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
output = '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(output)

# 7.1.1. Formatted String Literals
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# 7.1.2. The String format() Method
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


table = {k: str(v) for k, v in vars().items()}
# print('table = {}'.format(table))
# print(table)
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
# print(message)
print(message.format(**table))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 7.1.3. Manual String Formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))

# 7.1.4. Old string formatting
import math
print(math.pi)
print('%.3f' % math.pi)
print('The value of pi is approximately %5.3f.' % 9.1)

# 7.2. Reading and Writing Files

# 11.1. Output Formatting
import reprlib

reprlib_repr = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(reprlib_repr)


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint_pprint = pprint.pprint(t, width=30)
print(pprint_pprint)


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))


import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
format_string = locale.format_string("%d", x, grouping=True)
print(format_string)

string = locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)

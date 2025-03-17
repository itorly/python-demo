# 10.2. File Wildcards
import glob

glob_py = glob.glob('*.py')
print(glob_py)

# 10.3. Command Line Arguments

# Here is the output from running python demo.py one two three at the command line:

# ['demo.py', 'one', 'two', 'three']
# File demo.py
import sys
print(sys.argv)

# When run at the command line with python top.py --lines=5 alpha.txt beta.txt
# , the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].

import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
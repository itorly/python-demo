import os
wd = os.getcwd()      # Return the current working directory
print(wd)
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

# the built-in dir() and help() functions
dir = dir(os)
print(dir)

help(os)

# shutil module: file and directory management
import shutil
shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')
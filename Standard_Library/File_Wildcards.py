# # 10.2. File Wildcards
# import glob
#
# glob_py = glob.glob('*.py')
# print(glob_py)
#
# # 10.3. Command Line Arguments
#
# # Here is the output from running python demo.py one two three at the command line:
#
# # ['demo.py', 'one', 'two', 'three']
# # File demo.py
# import sys
# print(sys.argv)
#
# # When run at the command line with python top.py --lines=5 alpha.txt beta.txt
# # , the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].
#
# import argparse
#
# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)
#
#
# # 10.5. String Pattern Matching
# import re
#
# findall = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# print(findall)
#
# sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# print(sub)
#
# replace = 'tea for too'.replace('too', 'two')
# print(replace)
#
#
# # 10.6. Mathematics
# import math
#
# cos = math.cos(math.pi / 4)
# print(cos)
#
# log = math.log(1024, 2)
# print(log)
#
# import random
#
# choice = random.choice(['apple', 'pear', 'banana'])
# print(choice)
#
# sample = random.sample(range(100), 10)      # sampling without replacement
# print(sample)
#
# random = random.random()    # random float
# print(random)
#
# randrange = random.randrange(6)     # random integer chosen from range(6)
#
# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# mean = statistics.mean(data)
# print(mean)
#
# median = statistics.median(data)
# print(median)
#
# variance = statistics.variance(data)
# print(variance)
#
#
# # 10.7. Internet Access
# from urllib.request import urlopen
# # with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
# with urlopen('http://cn.bing.com/') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         print(line.rstrip())
#
#
#
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()


# # 10.8. Dates and Times
# # dates are easily constructed and formatted
# from datetime import date
# now = date.today()
# print(now)
#
# strftime = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(strftime)
#
# birthday = date(1964, 7, 31)
# age = now - birthday
# days = age.days
# print(days)


# 10.9. Data Compression
import zlib
s = b'witch which has which witches wrist watch'
len_s = len(s)
print(len_s)

t = zlib.compress(s)
len_t = len(t)
print(len_t)

decompress= zlib.decompress(t)
print(decompress)

crc32 = zlib.crc32(s)
print(crc32)

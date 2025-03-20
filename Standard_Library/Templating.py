# 11.2. Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
substitute = t.substitute(village='Nottingham', cause='the ditch fund')
print(substitute)


t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t_substitute = t.substitute(d)
print(t_substitute)

safe_substitute = t.safe_substitute(d)
print(safe_substitute)


import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
print('fmt=', fmt)

t = BatchRename(fmt)
print('t=', t)
date = time.strftime('%d%b%y')
print('date=', date)
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d = date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
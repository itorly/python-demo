# 11.6. Weak References
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
primary_ = d['primary']
print('primary_=', primary_)                # fetch the object if it is still alive

del a                       # remove the one reference
collect = gc.collect()      # run garbage collection right away
print("collected:", collect)

primary_2 = d['primary']               # entry was automatically removed
print('primary_2=', primary_2)

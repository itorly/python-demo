# 11.7. Tools for Working with Lists
from array import array
a = array('H', [4000, 10, 700, 22222])
sum = sum(a)
print(sum)

a_ = a[1:3]
print(a_)


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
# 11.7. Tools for Working with Lists
# from array import array
# a = array('H', [4000, 10, 700, 22222])
# sum = sum(a)
# print(sum)
#
# a_ = a[1:3]
# print(a_)
#
#
# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())


# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
heap_ = [heappop(data) for i in range(3)]  # fetch the three smallest entries
print(heap_)
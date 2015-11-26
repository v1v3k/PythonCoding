__author__ = 'george'

from collections import deque

queue = deque([1,2,3,4,5,6,7])

queue.append(10)
print(queue)

print queue.popleft()

queue.appendleft(11)
print queue

queue.clear()
print queue

queue= deque([1,2,3,4,5,6,7])

queue.reverse()
print queue

queue.extendleft([1,2,3])
print queue

queue.rotate(3)
print queue

queue.rotate(-3)
print queue
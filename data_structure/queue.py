from collections import deque

queue = deque()

queue.append(55)
queue.append(1)
queue.append(24)
queue.append(8)
queue.popleft()
queue.append(5)
queue.append(9)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

"""
출력 결과:
deque([24, 8, 5, 9])
deque([9, 5, 8, 24])
"""
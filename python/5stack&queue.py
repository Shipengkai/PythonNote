#   [1, 2, 3, 4, ..., 999, 1000]
# ->[2, 3, 4, 5, ..., 1000]
#   删除‘1’，需要移动999个


from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

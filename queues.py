# queues is another data structures which works of FIFO principle
from collections import deque
import queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.popleft()
print(queue)
if not queue:
    print('empty')

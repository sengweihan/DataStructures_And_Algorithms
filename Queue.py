#  queue data structures
from collections import deque

"""
Deque uses doubly linked list implementation 

OPERATION

    ---> Accessing arbitrary items through indexing = O(N)
    ---> Popping and appending items on the left end = O(1)
    ---> Popping and appending items on the right end = O(1)
    ---> Inserting and deleting items in the middle = O(N)
"""


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.append(value)

    def dequeue(self):
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == '__main__':
    pq = Queue()

    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    print(pq.size())
    print(pq.dequeue())

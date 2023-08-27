#  stack data structures
from collections import deque
"""
Deque uses doubly linked list implementation 

OPERATION

    ---> Accessing arbitrary items through indexing = O(N)
    ---> Popping and appending items on the left end = O(1)
    ---> Popping and appending items on the right end = O(1)
    ---> Inserting and deleting items in the middle = O(N)
"""


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

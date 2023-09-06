"""
HEAP CONSTRUCTION

 ---> HEAP CAN BE USED TO IMPLEMENT PRIORITY QUEUE (QUEUE WITH A CERTAIN PRIORITY WHETHER ITS MAX OR MIN)
 ---> CONSIST OF BOTH MIN-HEAP (CHILD >= PARENT) AND MAX-HEAP (PARENT >= CHILD)
 ---> BOTTOM UP CONSTRUCTION OF HEAP : TIME COMPLEXITY = O(N)
 ---> USUAL CONSTRUCTIONS = O(N LOG N), LOOP THROUGH EACH ELEMENT FOR N TIMES AND CALL RISE.
"""


class Heap:
    def __init__(self, max_element, array):
        # initilize the heap array (index 0 is empty) for easy calculations
        self.heap = [None] * (max_element + 1)
        self.length = max_element
        self.previous = None

        if array:
            for i in range(self.length):
                self.heap[i+1] = array[i]

            for i in range(max_element//2, 0, -1):
                self.sink(i)

    def sink(self, k):
        while 2 * k <= self.length:
            child_index = self.find_largest(k)
            if self.heap[k] >= self.heap[child_index]:
                break
            self.swap(k, child_index)
            k = child_index

    def find_largest(self, k):
        if 2 * k == self.length or self.heap[2*k] > self.heap[2*k + 1]:
            return 2*k
        else:
            return 2*k + 1

    def swap(self, k, child_index):
        self.heap[k], self.heap[child_index] = self.heap[child_index], self.heap[k]

    def get_max(self):
        max_element = self.heap[1]
        self.heap[1] = self.heap[self.length]
        self.heap[self.length] = None
        self.previous = self.length
        self.minus_length()
        self.sink(1)
        return max_element

    def minus_length(self):
        self.length -= 1

    def heap_sort(self):

        for i in range(self.length):
            max = self.get_max()
            self.heap[self.previous] = max


if __name__ == "__main__":
    x = Heap(7, [1, 9, 12, 5, 17, 15, 2])
    x.heap_sort()
    print(x.heap)

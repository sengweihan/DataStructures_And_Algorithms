# Binary Search Algorithm
"""
LINEAR SEARCH: TIME-COMPLEXITY = O(N)
BINARY SEARCH: TIME-COMPLEXITY = O(LOG N)

"""


def binary_search(lst, key):
    left = 0
    right = len(lst)-1

    while left <= right:
        mid_index = (left+right)//2
        element = lst[mid_index]

        if element == key:
            return mid_index
        elif element < key:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1


if __name__ == '__main__':
    lst = [12, 15, 17, 19, 21, 24, 45, 67]
    key = 200
    print("Number found at index " +
          str(binary_search(lst, key)) + " using binary search.")

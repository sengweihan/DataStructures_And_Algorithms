# Selection Sort Algorithm

"""
Time Complexity: O(N^2)
"""


def selectionSort(lst):

    for i in range(len(lst)-1):
        min_index = i

        for j in range(min_index+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # little optimization (if same index meaning that the item is minimum, then no need to swap among itself)
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


if __name__ == "__main__":
    print(selectionSort([5, 4, 3, 2, 1]))

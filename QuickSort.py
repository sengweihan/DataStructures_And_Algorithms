"""
Average Time Complexity For QuickSort is O(N LOG N)

Worst Case Time Complexity is O(N^2) when the array is already sorted
"""


def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(elements, start, end_index):
    pivot_index = start
    pivot_element = elements[pivot_index]

    start_index = pivot_index + 1

    while start_index < end_index:

        while start_index < len(elements) and elements[start_index] < pivot_element:
            start_index += 1

        while elements[end_index] > pivot_element:
            end_index -= 1

        if start_index < end_index:
            swap(start_index, end_index, elements)

    swap(pivot_index, end_index, elements)

    return end_index


def quicksort(elements, start, end):
    # hoare partition
    if start < end:
        pi = partition(elements, start, end)
        quicksort(elements, start, pi - 1)
        quicksort(elements, pi+1, end)


if __name__ == "__main__":
    # elements = [11, 9, 29, 7, 2, 15, 28]
    elements = [25, 22, 21, 10]

    quicksort(elements, 0, len(elements)-1)

    print(elements)

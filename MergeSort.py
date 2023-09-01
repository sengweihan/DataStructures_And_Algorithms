"""
Merge Sort Time Complexity : O(N LOG N)
"""


def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_array = lst[:mid]
    right_array = lst[mid:]

    left = merge_sort(left_array)
    right = merge_sort(right_array)

    return merge_two_array(left, right)


def merge_two_array(array1, array2):
    lst = []
    i = j = 0
    array1_length = len(array1)
    array2_length = len(array2)

    while i < array1_length and j < array2_length:
        if array1[i] < array2[j]:
            lst.append(array1[i])
            i += 1
        else:
            lst.append(array2[j])
            j += 1

    while i < array1_length:
        lst.append(array1[i])
        i += 1

    while j < array2_length:
        lst.append(array2[j])
        j += 1
    return lst


if __name__ == "__main__":
    print(merge_two_array([17, 21, 29, 38], [4, 9, 25, 32]))
    print(merge_sort([10, 3, 15, 7, 8, 23, 98, 29]))

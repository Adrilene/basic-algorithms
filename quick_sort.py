from utils import swap


def partition(elements_list, start, end):
    x = elements_list[end]
    i = start - 1
    for j in range(start, end):
        if elements_list[j] <= x:
            i = i + 1
            elements_list = swap(elements_list, i, j)

    elements_list = swap(elements_list, i + 1, end)
    return i + 1


def quick_sort(elements_list, start, end):
    if start <= end:
        q = partition(elements_list, start, end)
        quick_sort(elements_list, start, q - 1)
        quick_sort(elements_list, q + 1, end)

    return elements_list

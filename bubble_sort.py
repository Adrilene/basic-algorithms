from utils import swap


def bubble_sort(elements_list):
    for i in range(len(elements_list)):
        for j in range(i + 1, len(elements_list)):
            if elements_list[j] < elements_list[i]:
                elements_list = swap(elements_list, i, j)

    return elements_list

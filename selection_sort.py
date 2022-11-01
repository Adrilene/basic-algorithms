from utils import swap


def get_min_index(elements_list, index):
    min_index = index
    for i in range(index + 1, len(elements_list)):
        if elements_list[i] < elements_list[min_index]:
            min_index = i

    return min_index


def selection_sort(elements_list):
    for i in range(len(elements_list)):
        min_index = get_min_index(elements_list, i)
        if elements_list[min_index] < elements_list[i]:
            elements_list = swap(elements_list, i, min_index)

    return elements_list

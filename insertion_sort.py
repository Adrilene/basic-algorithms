def shift(elements_list, index_a, index_b):
    aux = elements_list[index_b]
    for i in range(index_b, index_a, -1):
        elements_list[i] = elements_list[i - 1]

    elements_list[index_a] = aux

    return elements_list


def insertion_sort(elements_list):
    for i in range(1, len(elements_list)):
        for j in range(0, i):
            if elements_list[i] < elements_list[j]:
                elements_list = shift(elements_list, j, i)

    return elements_list

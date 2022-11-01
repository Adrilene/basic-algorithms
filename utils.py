def swap(elements_list, index_a, index_b):
    aux = elements_list[index_a]
    elements_list[index_a] = elements_list[index_b]
    elements_list[index_b] = aux
    return elements_list

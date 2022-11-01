from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort


def main():
    elements_list = [5, 4, 6, 1, 60, 7, 2, 12]
    print(quick_sort(elements_list, 0, 7))


if __name__ == "__main__":
    main()

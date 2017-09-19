from random import shuffle


# Sorts a list using bubble sort.
def bubble_sort(alist):
    is_sorted = False

    while not is_sorted:
        num_of_swaps = False

        for num in range(0, len(alist) - 1):

            if alist[num] > alist[num + 1]:
                alist[num], alist[num + 1] = alist[num + 1], alist[num]
                num_of_swaps += 1

        if num_of_swaps == 0:
            is_sorted = True

    return print(alist)


wonky_list = [[i] for i in range(10000)]
shuffle(wonky_list)

bubble_sort(wonky_list)

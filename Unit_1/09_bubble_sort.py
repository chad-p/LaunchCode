

from random import shuffle


# Sorts a list using bubble sort.
def bubble_sort(alist):
    is_sorted = False
    len_alist = len(alist) - 1

    while not is_sorted:
        num_of_swaps = False

        for num in range(0, len_alist):

            if alist[num] > alist[num + 1]:
                alist[num], alist[num + 1] = alist[num + 1], alist[num]
                num_of_swaps += 1

        len_alist -= 1

        if num_of_swaps == 0:
            is_sorted = True

    return alist


wonky_list = [[i] for i in range(10)]
shuffle(wonky_list)

print(bubble_sort(wonky_list))

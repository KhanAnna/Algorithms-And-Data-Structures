from array import array


def bubble_sort_v1(array) -> array:
    N = len(array)
    i = 0
    IS_SORTED = False
    while not IS_SORTED:
        IS_SORTED = True
        for j in range(0, N - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]   
                IS_SORTED = False 
        i+=1

    return array


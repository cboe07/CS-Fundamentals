# Implement the insertion sort algorithm in the insertion_sort method.
# Return the sorted array.

# Helpful Resources:
# https://www.youtube.com/watch?v=DFG-XuyPYUQ&t=9s
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
#

def insertion_sort(my_array):
    array_length = len(my_array)

    for i in range(1, array_length):
        current_value = my_array[i]
        j = i

        while j > 0 and my_array[j - 1] > current_value:
            my_array[j] = my_array[j - 1]
            j = j - 1

        my_array[j] = current_value

    return my_array

input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = insertion_sort(array)
    print("Output: " + str(sorted_array))


def insertion(array):
    for i in range(1, len(array)):
        temp = array[i]
        while j > 0 & j > array[j -1]















































def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
unsorted_array = [5, 9, 2, 1, 67, 34, 88, 34]
bubble_sort(unsorted_array)
print(unsorted_array)

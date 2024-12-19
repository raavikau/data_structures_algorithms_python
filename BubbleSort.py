# compare and swap two adjacent elements until they are unsorted

def bubble_sort(array):
    for i in range(len(array)):  # loop through each element of array
        swapped = False  # keep track of swapping
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:  # compare two adjacent elements
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:  # means the array is already sorted
            break

unsorted_array = [5, 9, 2, 1, 67, 34, 88, 34]
# unsorted_array = [1, 2, 3, 4, 2]
# unsorted_array = ["mona", "dhaval", "aamir", "tina", "chang"]
bubble_sort(unsorted_array)
print(unsorted_array)

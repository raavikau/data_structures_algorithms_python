# first selects a pivot element & partitions the list around the pivot, putting every smaller element left side & every
# larger element on right side of pivot recursively sort each array

def partition(numbers, start, end):  # find the partition position
    pivot = numbers[end]  # rightmost element as pivot
    i = start-1  # pointer for greater element
    for j in range(start, end):
        if numbers[j] <= pivot:  # compare element with pivot if element smaller than pivot found
            i += 1  # then swap it with the greater element pointed by i
            numbers[i], numbers[j] = numbers[j], numbers[i]  # swapping element at i with element at j
    numbers[i+1], numbers[end] = numbers[end], numbers[i+1]  # swap the pivot element with the greater element specified by i
    return i+1  # return the position to pi variable where partition is done
def quick_sort(numbers, start, end):
    if start < end:
        pi = partition(numbers, start, end)  # find pivot element smaller than pivot on left ,greater than pivot are on right
        quick_sort(numbers, start, pi - 1)  # recursive call on the left side of pivot
        quick_sort(numbers, pi + 1, end)  # recursive call on the right side of pivot

unsorted_list = [8, 7, 2, 1, 0, 9, 6]
size = len(unsorted_list)
quick_sort(unsorted_list, 0, size-1)
print(unsorted_list)


def mergeSort(array):
    if len(array) > 1:
        median = len(array)//2
        left = array[:median]
        right = array[median:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k]= right[j]
            j += 1
            k += 1

def display(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
unsorted_array = [6, 5, 12, 10, 9, 1]
mergeSort(unsorted_array)
print("Sorted array is: ")
display(unsorted_array)

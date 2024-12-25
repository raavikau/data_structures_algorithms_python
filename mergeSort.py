# dividing a problem into multiple sub-problems. Each sub-problem is then solved individually. Finally, sub-problems
# are combined to form the final solution

def mergeSort(array):
    if len(array) > 1:
        median = len(array)//2  # median is the pt the array is divided into two sub arrays
        left = array[:median]
        right = array[median:]
        mergeSort(left)  # sort the left half
        mergeSort(right)  # sort the right half
        i = j = k = 0  # i is index for left, j for right, k index for sorted array
        while i < len(left) and j < len(right):  # loop until we reach end of either left or right
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):  # pickup the remaining elements and put in array
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k]= right[j]
            j += 1
            k += 1

def display(array):  # different way to display array
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
unsorted_array = [6, 5, 12, 10, 9, 1]
mergeSort(unsorted_array)
print("Sorted array is: ")
display(unsorted_array)

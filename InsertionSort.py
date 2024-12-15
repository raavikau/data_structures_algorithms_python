def insertionSort(array):
    for index in range(1, len(array)):
        key = array[index]
        previndex = index - 1
        while previndex >= 0 and key < array[previndex]:
            array[previndex + 1] = array[previndex]
            previndex = previndex - 1
        array[previndex + 1] = key

unsorted_array = [9, 15, 1, 4, 3]
insertionSort(unsorted_array)
print('Sorted Array in Ascending Order:', unsorted_array)

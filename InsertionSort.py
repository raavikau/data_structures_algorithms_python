# An element from unsorted part is picked and is placed at correct position in the sorted part
# places an unsorted element at its suitable place in each iteration

def insertionSort(array):
    for index in range(1, len(array)):  # first element in the array is assumed to be sorted
        key = array[index]  # take the second element and store it as key
        previndex = index - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while previndex >= 0 and key < array[previndex]:
            array[previndex + 1] = array[previndex]
            previndex = previndex - 1

        array[previndex + 1] = key  # place key after the element just smaller than it

unsorted_array = [9, 15, 1, 4, 3]
insertionSort(unsorted_array)
print('Sorted Array in Ascending Order:', unsorted_array)

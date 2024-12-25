# select the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
import time
def selectionSort(numbers):
    for i in range(len(numbers)-1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if numbers[j] < numbers[min_index]:
                min_index = j
        if i != min_index:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # put min value at the correct position
unsort_list = [18, 6, 66, 44, 9, 22, 14]
before_time = time.time()
selectionSort(unsort_list)
current_time = time.time()
run_time = current_time - before_time

print(run_time)
print("Sorted list", unsort_list)

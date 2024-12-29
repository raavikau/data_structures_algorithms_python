
def partition(numbers, start, end):
    pivot = numbers[end]
    i = start-1
    for j in range(start, end):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[end] = numbers[end], numbers[i+1]
    return i+1

def quick_sort(numbers, start, end):
    if start < end:
        pi = partition(numbers, start, end)
        quick_sort(numbers, 0, pi-1)
        quick_sort(numbers, pi+1, end)

unsorted_list = [8, 7, 2, 1, 0, 9, 6]
size = len(unsorted_list)
quick_sort(unsorted_list, 0, size-1)
print(unsorted_list)

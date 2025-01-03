# the element is always search in the middle of a portion of sorted array.
def binary_search(number, target):
    first = 0
    last = len(number) -1
    while first <= last:      # Repeat until the pointers first and last meet each other
        median = (first + last) // 2
        if number[median] == target:
            return median
        elif number[median] < target:
            first = median + 1
        else:
            last = median - 1
    return None
def display(index):
    if index is not None:
        print("Target is at ", index)
    else:
        print("Target value is not find")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(data, 8)
display(result)

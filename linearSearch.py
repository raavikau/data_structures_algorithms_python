def linear_search(numbers, target):
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return None
def display(index):
    if index is not None:
        print("Target value index is", index)
    else:
        print("Target not found")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
result = linear_search(data, 11)
display(result)

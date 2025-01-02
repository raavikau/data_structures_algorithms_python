def recursive_binary(number, target):
    if len(number) == 0:
        return False
    else:
        midpoint = len(number) // 2
        if number[midpoint] == target:
            return True
        else:
            if number[midpoint] < target:
                return recursive_binary(number[midpoint + 1:], target)
            else:
                return recursive_binary(number[: midpoint - 1], target)

def display(result):
    if result is False:
        print("Target not found")
    else:
        print("Target found")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = recursive_binary(data, 4)
display(results)

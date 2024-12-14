def selection(numbers):
    for i in range(len(numbers)-1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        if i != min_index:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
unsort_list = [18, 6, 66, 44, 9, 22, 14]
selection(unsort_list)

print("Sorted list", unsort_list)

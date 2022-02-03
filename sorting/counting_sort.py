def counting_sort(arr):
    max_value = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    count_arr = [0]*(max_value+1)
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i] + count_arr[i-1]
    sorted_arr = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        count_arr[arr[i]] -= 1
        sorted_arr[count_arr[arr[i]]] = arr[i]
    return sorted_arr


print(counting_sort([2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]))
print(counting_sort([12, 11, 13, 5, 6, 10]))
print(counting_sort([7, 4, 10, 8, 3, 1]))

# Time Complexity
# Best, Average, Worst = O(n+k)

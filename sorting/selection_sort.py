def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if a[j] < a[min_index]:
                min_index = j
        arr[i], a[min_index] = arr[min_index], a[i]
    return arr


print(selection_sort([12, 11, 13, 5, 6, 10]))
print(selection_sort([7, 4, 10, 8, 3, 1]))

# Time complexity
#Best, Average, Worst = O(n^2)

''' 
1)Set MIN to location 0
2)Search the minimum element in the list
3)Swap with value at location MIN
4)Increment MIN to point to next element
5)Repeat until list is sorted
'''

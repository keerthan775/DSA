def bubble_sort(arr):
    for i in range(len(arr)):
        is_swap = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                is_swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not is_swap:
            break
    return arr


print(bubble_sort([12, 11, 13, 5, 6, 10]))
# Time Complexity
# best = O(n)
# average, worst = O(n^2)

'''
1)Iterate from arr[0] to arr[n] over the array. 
2)if current element is greater than next then swap
3)continue
 '''

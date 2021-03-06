def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr


print(insertion_sort([12, 11, 13, 5, 6, 10]))

# Time Complexity
#Best = O(n)
#Average, Worst = O(n^2)


''' 
1)Iterate from arr[1] to arr[n] over the array. 
2)Compare the current element (key) to its predecessor. 
3)If the key element is smaller than its predecessor, compare it to the elements before.
  Move the greater elements one position up to make space for the swapped element.
'''

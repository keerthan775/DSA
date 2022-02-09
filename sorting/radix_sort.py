def radix_sort(arr):
    max_value = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    pos = 1
    sorted_arr = None
    while max_value//pos>0:
        sorted_arr = counting_sort(arr, len(arr), pos)
        pos *= 10
    return sorted_arr
    
def counting_sort(arr, n, pos):
    count_arr = [0] * 10
    for i in range(n):
        count_arr[(arr[i]//pos)%10] +=  1
    for i in range(1,n):
        count_arr[i] = count_arr[i] + count_arr[i-1]
    output_arr = [0] * 10
    for i in range(n-1,-1,-1):
        output_arr[count_arr[(arr[i]//pos)%10 ]-1 ] = arr[i]
        count_arr[(arr[i]//pos)%10 ] -= 1
    for i in range(len(arr)):
        arr[i] = output_arr[i]
    return arr
    
print(radix_sort([432,8,530,90,88,231,11,45,677,199]))

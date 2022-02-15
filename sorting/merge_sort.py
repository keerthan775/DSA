def merge_sort(arr):
    merge_sort_divide(arr,0 , len(arr)-1)
    return arr

def merge_sort_divide(arr, lb, ub):
    if(lb<ub):
        mid = (lb+ub)//2
        merge_sort_divide(arr, lb, mid)
        merge_sort_divide(arr, mid+1, ub)
        merge_sort_conquer(arr, lb, mid, ub)
    

def merge_sort_conquer(arr, lb, mid, ub):
    i = lb
    j = mid+1
    k = lb
    b = [0] * (ub + 1)
    while(i<=mid and j<=ub):
        if(arr[i] <= arr[j]):
            b[k] = arr[i]
            i += 1
            k += 1
        else:
            b[k] = arr[j]
            j += 1
            k += 1
    if(i>mid):
        while(j<=ub):
            b[k] = arr[j]
            k += 1
            j += 1
    else:
        while(i<=mid):
            b[k] = arr[i]
            i += 1
            k += 1
    for i in range(lb,ub+1):
        arr[i] = b[i]

print(merge_sort([15, 5, 24, 8, 1, 3, 6, 10, 20]))
print(merge_sort([12, 11, 13, 5, 6, 10]))

def quick_sort(arr):
    return quick_sort_main(arr, 0, len(arr)-1)

def quick_sort_main(arr, lb, ub):
    if(lb < ub):
        loc = partition(arr, lb, ub)
        quick_sort_main(arr, lb, loc-1)
        quick_sort_main(arr, loc+1, ub)
    return arr

def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb 
    end   = ub
    while(start<end ):
        while(arr[start]<=pivot and start != ub):
            start += 1 
        while(arr[end]>pivot and end != lb):
            end -= 1 
        if(start<end):
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end

print(quick_sort([7, 6, 10, 5, 9, 2, 1, 15, 7]))
import sys
sys.path.append('../')
from sorting.quick_sort import *

def binary_search_main(arr, l, h ,search_val):
    if l<=h:
        mid = (l+h)//2
        if arr[mid] == search_val:
            return mid
        elif arr[mid] > search_val:
            return binary_search_main(arr, l, mid-1, search_val)
        else:
            return binary_search_main(arr, mid+1, h, search_val)
    else:
        return None

def binary_search(arr, search_value):
    return binary_search_main(arr, 0, len(arr)-1, search_value)


print(binary_search(quick_sort([1,9,2,3,11,10,25,21]),3))
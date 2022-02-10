from insertion_sort import *
def bucket_sort(arr):
    num  = 10
    arr2 = [] 
    for i in range(num):
        arr2.append([])
    for i in arr:
        arr2[int(i*10)].append(i)
    print(arr2)
    for i in range(len(arr2)):
        arr2[i] = insertion_sort(arr2[i])
    print(arr2)
bucket_sort([0.897, 0.565, 0.665, 0.1234, 0.656, 0.3434, 0.11])
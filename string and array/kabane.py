import time
#l = [-3, -4, -5, -1, 2, -4, 6, -1]
l = [-2, -3, 4, -1, -2, 1, 5, -3]
#l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# brute force
def brute_force(l):
    max_value = 0
    max_index = 0
    min_index = 0
    for i in range(len(l)):
        sum_value = 0 
        for j in range(i, len(l)):
            #print(l[i:j])
            sum_value += l[j]
            if sum_value>max_value:
                max_value = sum_value
                max_index = j
                if i != max_index:
                    min_index = i
        
        #print()
    #print(d)
    print(max_value)
    print(min_index, max_index)
start_time = time.time()
brute_force(l)
print("time taken",time.time()-start_time)

# kabane's algorithm
def kabane(l):
    temp = max_value = 0
    min_index = 0
    max_index = 0
    temp_index = 0
    for i in range(len(l)):
        temp = temp + l[i]
        if temp < 0:
            temp = 0
            temp_index = i +1 
        if max_value < temp :
            max_index = i
            max_value = temp
            min_index = temp_index
        #if temp==max_value and temp!=0:
        #    if min_index == 0:
        #        min_index = i
    print(max_value)
    print(min_index,max_index)
start_time = time.time()
kabane(l)
print("time taken",time.time()-start_time)
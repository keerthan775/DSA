# Normal approach
def fibo_normal(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fibo_normal(n-1) + fibo_normal(n-2)
#O(2^n)

#-----------Dynamic programming approach-----------
#Top down approach or recursion

def fibo_tpa(n,memoization_list):
    if memoization_list[n]:
        return memoization_list[n] 
    else:
        if(n==0):
            return 0
        if(n==1):
            return 1
        memoization_list[n] = fibo_tpa(n-1,memoization_list) + fibo_tpa(n-2,memoization_list)
        return memoization_list[n]

def fibo_tpa_main(n):
    memoization_list = [None]*(n+1)
    memoization_list[0] = 0
    memoization_list[1] = 1
    return fibo_tpa(n,memoization_list)
#O(n)

#Bottom up approach or iterative
def fibo_bua(n):
    arr = [None]*(n+1)
    arr[0:1] = 0,1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]
#O(n)

if __name__ == "__main__":
    print(fibo_normal(6))
    print(fibo_tpa_main(6))
    print(fibo_bua(6))
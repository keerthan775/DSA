def coin_change(coins, amount):
    arr = [[0]*(amount+1)]*len(coins)
    for i in range(len(coins)):
        for j in range(amount+1):
            if(j==0):
                arr[i][j] = 1
            if(i==0 and j>0):
                if(j>=coins[i] and j%coins[0]==0):
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
            elif(i>0 and coins[i]>j):
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-coins[i]]
        

coin_change([2,3,5,10],15)

def maxProfit(prices):
    # create a mapping between a price and its index 
    # next we are going to sort prices 
    m = []
    n = len(prices)
    m = [0 for _ in range(len(prices)+1)]
    for i in range(1,n):
        for j in range(i+1,n):
            m[i] = max(prices[j]-prices[i],m[i-1])
    print(m)
    return m[n] 


print(maxProfit([7,6,4,3,1]))


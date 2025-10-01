class Solution:
    def trades_history(self,prices):
        maxP = 0.00
        l,r=2,3
        buy,sell = None,None

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
                buy,sell = prices[l],prices[r]
            else:
                l=r
            r+=1
        buys = f"Buy at: {buy}"
        sells = f"Sell at: {sell}"
        return maxP,buys,sells

coins = Solution()
expection = coins.trades_history([
    0.8092, 
    0.8304,  
    0.8182,
    0.8351, 
    0.8651, 
    0.8650, 
    0.8852, 
    0.8939, 
    0.9170, 
    0.9295, 
    0.8879, 
    0.8633
]
)
print(expection[0])
print(expection[1])
print(expection[2])
        
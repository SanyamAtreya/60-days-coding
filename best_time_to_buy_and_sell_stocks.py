class Solution(object):
    def maxProfit(self, prices):
        diff = 0
        buy = prices[0]
        i = 0
        while(i < len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                diff = max(profit, diff)
            i += 1
        
        return diff

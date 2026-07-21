class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        pri = 0
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                pri = prices[r] - prices[l]
                maxP = max(maxP,pri)
            else:
                l = r
            r += 1
        return maxP
        
        

'''
brute force
    2 pointer where you loop through each num 
    O(n^2)

Sliding window
    left side buy
    right side sell
    
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        maxProfit = 0 # return if we cant find anything also
        l = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                # curr price is lower than our lowest we seen
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
            # we reset to the lowest and find the res each time, the highest res is stored

        return maxProfit



        
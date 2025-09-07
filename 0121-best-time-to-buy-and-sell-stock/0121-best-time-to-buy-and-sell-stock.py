class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = float('inf')
        # can set to 0 bc if we dont sell its still 0

        for i, num in enumerate(prices):
                lowest = min(lowest, num)
                max_profit = max(max_profit, num - lowest)

        return max_profit
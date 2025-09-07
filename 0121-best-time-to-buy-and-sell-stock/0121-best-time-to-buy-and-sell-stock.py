class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = float('inf')
        # can set to 0 bc if we dont sell its still 0

        for i, num in enumerate(prices):
            if num < lowest:
                lowest = num

            temp_profit = num - lowest
            if max_profit < temp_profit:
                max_profit = temp_profit

        return max_profit
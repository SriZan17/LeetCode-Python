class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max_profit = 0
        for p in prices:
            if p < min:
                min = p
            elif (p - min) > max_profit:
                max_profit = p - min
        return max_profit

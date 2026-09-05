class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        small = prices[0]
        

        for i in range(1, len(prices)):
            if prices[i] < small:
                small = prices[i]

            temp = prices[i] - small

            if temp > best:
                best = temp


        return best

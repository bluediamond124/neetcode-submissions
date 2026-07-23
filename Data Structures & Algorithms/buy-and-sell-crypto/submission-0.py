class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you can start by trying to find an apex after the min
        minima=prices[0]
        profit=0
        for i in range(len(prices)):
            # what if the current is less than the minima
            if prices[i]<minima:
                minima=prices[i]
            if prices[i]-minima>profit:
                profit=prices[i]-minima
        return profit
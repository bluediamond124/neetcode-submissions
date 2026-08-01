class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is going to be the min amount of coins to get to this
        if min(coins)>amount and amount!=0: return -1
        if amount==0: return 0
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1

        
class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        mp = 0

        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]

            cp = prices[i] - buy
            mp = max(mp, cp)

        return mp


prices = [7, 1, 5, 3, 6, 4]

obj = Solution()
print(obj.maxProfit(prices))
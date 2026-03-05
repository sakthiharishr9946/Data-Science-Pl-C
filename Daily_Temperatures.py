class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

obj = Solution()
result = obj.dailyTemperatures(temperatures)

print(result)
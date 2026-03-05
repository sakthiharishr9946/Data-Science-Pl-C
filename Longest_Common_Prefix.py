class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first = strs[0]
        last = strs[-1]
        result = []
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            result.append(first[i])
        return "".join(result)

strs = ["flower", "flow", "flight"]

obj = Solution()
print(obj.longestCommonPrefix(strs))
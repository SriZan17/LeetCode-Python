class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        a = 0
        while True:
            for i in range(n):
                try:
                    if strs[i][a] != strs[0][a]:
                        return strs[i][:a]
                except IndexError:
                    return strs[i][:a]
            a = a + 1

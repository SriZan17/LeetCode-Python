class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while True:
            if i == len(s):
                return True
            elif j == len(t):
                return False
            if s[i] == t[j]:
                i = i + 1
            j = j + 1

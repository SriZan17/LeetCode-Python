class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s) - 1):
            curr_value = ord(s[i])
            next_value = ord(s[i + 1])
            score = score + abs(curr_value - next_value)
        return score

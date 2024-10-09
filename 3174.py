# pop at every num encounter and push at every letter
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalpha():
                stack.append(c)
            if c.isdigit():
                stack.pop()
        return "".join(stack)

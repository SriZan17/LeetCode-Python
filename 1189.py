class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        n = 0
        while True:
            count["b"] -= 1
            count["a"] -= 1
            count["l"] -= 2
            count["o"] -= 2
            count["n"] -= 1
            if (
                count["b"] >= 0
                and count["a"] >= 0
                and count["l"] >= 0
                and count["o"] >= 0
                and count["n"] >= 0
            ):
                n = n + 1
                continue
            else:
                return n

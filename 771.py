class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        hash = set(jewels)
        for stone in stones:
            if stone in hash:
                c = c + 1
        return c

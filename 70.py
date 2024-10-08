# using @cache automatically memoizes the results of the recursive function
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def get_step(n):
            if n < 0:
                return 0
            if n in [1, 2]:
                return n
            return get_step(n - 1) + get_step(n - 2)

        return get_step(n)

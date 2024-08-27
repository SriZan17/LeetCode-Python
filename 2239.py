class Solution:
    def findClosestNumber(self, nums) -> int:
        diff = nums[0]
        for n in nums:
            if abs(n) < abs(diff):
                diff = n
            elif abs(n) == abs(diff):
                if n > diff:
                    diff = n
        return diff

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = 0
        for i in range(k):
            total = total + nums[i]
        highest_total = total
        for i in range(k, n):
            total = total - nums[i - k]
            total = total + nums[i]
            if total > highest_total:
                highest_total = total
        return highest_total / k

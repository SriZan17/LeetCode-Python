# Deque data structure is used for faster insertion at the begining of the array.
# Two pointer approach is used.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        solution = deque()
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                solution.appendleft(nums[left] ** 2)
                left = left + 1
            else:
                solution.appendleft(nums[right] ** 2)
                right = right - 1
        return list(solution)
